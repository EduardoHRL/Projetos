from django.db import models


class TblTarefas(models.Model):
    tar_id = models.AutoField(primary_key=True)
    usu = models.ForeignKey('TblUsuario', on_delete=models.CASCADE, blank=True, null=True)
    tar_descricao = models.CharField(max_length=255, blank=True, null=True)
    tar_nomesetor = models.CharField(db_column='tar_nomeSetor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tar_prioridade = models.CharField(max_length=20, blank=True, null=True)
    tar_data = models.DateField(auto_now_add= True,blank=True, null=True)
    tar_status = models.CharField(max_length=20, blank=True, null=True, default='A fazer')

    class Meta:
        db_table = 'tbl_tarefas'


class TblUsuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nome = models.CharField(max_length=255, blank=True, null=True)
    usu_email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.usu_nome

    class Meta:
        db_table = 'tbl_usuario'
