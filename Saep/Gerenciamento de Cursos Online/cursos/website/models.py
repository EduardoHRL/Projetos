from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    carga_horaria = models.FloatField()
    instrutor = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome}"