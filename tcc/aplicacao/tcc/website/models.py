from django.db import models

class Usuarios(models.Model):
    usu_codigo = models.AutoField(primary_key=True, db_column='usu_codigo')
    usu_nome = models.CharField(max_length=255, db_column='usu_nome')
    usu_email = models.EmailField(max_length=255, db_column='usu_email')
    usu_cpf = models.CharField(max_length=14, db_column='usu_cpf', unique=True)
    usu_telefone = models.CharField(max_length=11, db_column='usu_telefone')
    usu_senha = models.CharField(max_length=255, db_column='usu_senha')
    usu_tipoUsuario = models.CharField(max_length=13, db_column='usu_tipoUsuario')
    
    def __str__(self):
        return self.usu_nome
    
    class Meta:
        db_table = 'tbl_usuarios'

class Laboratorios(models.Model):
    lab_codigo = models.AutoField(primary_key=True, db_column='lab_codigo')
    lab_nome = models.CharField(max_length=255, db_column='lab_nome')
    lab_descricao = models.TextField(db_column='lab_descricao')
    lab_capacidade = models.IntegerField(db_column='lab_capacidade')
    lab_status = models.CharField(max_length=45, db_column='lab_status')

    def __str__(self):
        return self.lab_nome

    class Meta:
        db_table = 'tbl_laboratorios'

class Reservas(models.Model):
    res_codigo = models.AutoField(primary_key=True, db_column='res_codigo')
    res_inicio = models.DateTimeField(db_column='res_inicio')
    res_fim = models.DateTimeField(db_column='res_fim')
    res_repeticao = models.BooleanField(db_column='res_repeticao', db_default=False)
    res_status = models.CharField(max_length=45, db_column='res_status')
    usuario = models.ForeignKey(
        Usuarios, on_delete=models.CASCADE, related_name='usuario', db_column='usu_codigo'
    )
    laboratorio = models.ForeignKey(
        Laboratorios, on_delete=models.CASCADE, related_name='laboratorio_reservas', db_column='lab_codigo_res'
    )

    class Meta:
        db_table = 'tbl_reservas'


class Equipamentos(models.Model):
    equip_codigo = models.AutoField(primary_key=True, db_column='equip_codigo')
    equip_nome = models.CharField(max_length=30, db_column='equip_nome')
    equip_descricao = models.TextField(db_column='equip_descricao')
    laboratorio = models.ForeignKey(
        Laboratorios, on_delete=models.CASCADE, related_name='laboratorio_equipamentos', db_column='lab_codigo_equip'
    )

    def __str__(self):
        return self.equip_nome
    
    class Meta:
        db_table = 'tbl_equipamentos'

class Horario_reserva(models.Model):
    hor_codigo = models.AutoField(primary_key=True, db_column='hor_codigo')
    hor_inicio = models.DateTimeField(db_column='hor_inicio')
    hor_fim = models.DateTimeField(db_column='hor_fim')
    hor_diasDisponiveis = models.DateField(db_column='hor_diasDisponiveis')
    laboratorio = models.ForeignKey(
        Laboratorios, on_delete=models.CASCADE, related_name='laboratorio_horario_reserva', db_column='lab_codigo_hor'
    )

    class Meta:
        db_table = 'tbl_horario_reserva'  

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.nome