from django.db import models

class tbl_usuarios(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    username = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    senha = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    objetos = models.Manager()