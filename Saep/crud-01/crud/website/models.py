from django.db import models


class Tarefas(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    nome_setor = models.CharField(max_length=100, blank=True, null=True)
    prioridade = models.CharField(max_length=45, blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=45, blank=True, null=True, default='A fazer')
    usuarios = models.ForeignKey('Usuarios',on_delete=models.CASCADE , db_column='Usuarios_id')

    class Meta:
        db_table = 'tarefas'


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome
