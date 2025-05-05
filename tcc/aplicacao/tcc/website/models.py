from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cpf_field.models import CPFField
from multiselectfield import MultiSelectField
from django.core.validators import FileExtensionValidator, MinLengthValidator
from simple_history.models import HistoricalRecords, HistoricForeignKey

DIAS_SEMANA = [
    (0, 'Segunda'),
    (1, 'Terça'),
    (2, 'Quarta'),
    (3, 'Quinta'),
    (4, 'Sexta'),
    (5, 'Sábado'),
    (6, 'Domingo'),
]

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("O superusuário precisa ter is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("O superusuário precisa ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class Usuarios(AbstractUser):
    email = models.EmailField(unique=True)
    cpf = CPFField('cpf')
    telefone = models.CharField(max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'tbl_usuarios'


class Equipamentos(models.Model):
    equip_codigo = models.AutoField(primary_key=True, db_column='equip_codigo')
    equip_nome = models.CharField(max_length=30, db_column='equip_nome')
    equip_descricao = models.TextField(db_column='equip_descricao')

    def __str__(self):
        return self.equip_nome
    
    class Meta:
        db_table = 'tbl_equipamentos'

class Laboratorios(models.Model):
    STATUS_ESCOLHA = [
        ('disponivel', 'Disponível'),
        ('usando', 'Em uso'),
        ('indisponivel', 'Indisponível')
    ]
    lab_codigo = models.AutoField(primary_key=True, db_column='lab_codigo')
    lab_nome = models.CharField(max_length=255, db_column='lab_nome')
    lab_descricao = models.TextField(blank=True, null=True, db_column='lab_descricao')
    lab_capacidade = models.IntegerField(db_column='lab_capacidade')
    lab_status = models.CharField(max_length=20, choices=STATUS_ESCOLHA, default='disponivel', db_column='lab_status')
    lab_foto = models.ImageField(default='icone_sala_aula.jpeg', blank=True, null=True, upload_to='uploads/')
    lab_equipamento = models.ManyToManyField(Equipamentos, through='LaboratorioEquipamento')

    def __str__(self):
        return self.lab_nome

    class Meta:
        db_table = 'tbl_laboratorios'

class LaboratorioEquipamento(models.Model):
    laboratorio = models.ForeignKey(Laboratorios, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('laboratorio', 'equipamento')

    def __str__(self):
        return f"{self.laboratorio.lab_nome} - {self.equipamento.equip_nome} ({self.quantidade})"

class Reservas(models.Model):
    REPETICAO_ESCOLHAS = [
        ('N', 'Não repetir'),
        ('D', 'Diariamente'),
        ('S', 'Semanalmente'),
        ('M', 'Mensalmente'),
        ('A', 'Anualmente'),
    ]
    res_codigo = models.AutoField(primary_key=True, db_column='res_codigo')
    res_inicio = models.DateTimeField(db_column='res_inicio')
    res_fim = models.DateTimeField(db_column='res_fim')
    res_repeticao = models.CharField(max_length=1, choices=REPETICAO_ESCOLHAS, default='N', db_column='res_repeticao')
    res_status = models.CharField(max_length=45, db_column='res_status')
    res_intervalo_semanas = models.PositiveIntegerField(null=True, blank=True, db_column='res_intervalo_semanas')
    res_dia_semana = models.JSONField(null=True, blank=True, db_column='res_dia_semana')
    res_data_final_repeticao = models.DateField(null=True, blank=True, db_column='res_data_final_repeticao')
    res_descricao = models.TextField(blank=True, db_column='res_descricao')
    laboratorio = models.ForeignKey(
        Laboratorios, on_delete=models.CASCADE, related_name='laboratorio_reservas', db_column='lab_codigo_res'
    )
    professor = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='professor', db_column='professor_codigo_reserva')
    res_repeticao_original = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='repeticoes', db_column='res_repeticao_original'
    )

    history = HistoricalRecords()
    class Meta:
        db_table = 'tbl_reservas'

class Disponibilidade(models.Model):
    hor_codigo = models.AutoField(primary_key=True, db_column='hor_codigo')
    hor_inicio = models.TimeField(db_column='hor_inicio')
    hor_fim = models.TimeField(db_column='hor_fim')
    hor_diasDisponiveis = MultiSelectField(choices=DIAS_SEMANA ,db_column='hor_diasDisponiveis')
    laboratorio = models.ForeignKey(
        Laboratorios, on_delete=models.CASCADE, related_name='disponibilidades', db_column='lab_codigo_hor'
    )

    class Meta:
        db_table = 'tbl_horario_reserva'

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.hor_inicio} às {self.hor_fim}"

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(default='sem_foto.jpeg', blank=True, upload_to='uploads/', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    cep = models.CharField(max_length=10, unique=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    bairro = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fim = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_escola'

    def __str__(self):
        return self.nome