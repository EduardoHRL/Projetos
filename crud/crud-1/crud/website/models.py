from django.db import models
from django.contrib.auth.models import AbstractUser

class Alunos(AbstractUser):
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self): 
        return self.username

class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()
    instrutor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Inscricoes(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('aluno', 'curso')

    def __str__(self):
        return f"{self.aluno} - {self.curso}"