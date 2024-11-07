from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()