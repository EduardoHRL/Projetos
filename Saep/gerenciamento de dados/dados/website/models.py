# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import CASCADE
from django.db import models


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=14,blank=True, null=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_pedido = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, db_column='cliente', blank=True, null=True)
    produto = models.ForeignKey('Produtos', on_delete=models.CASCADE, db_column='produto', blank=True, null=True)

    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f"Pedido de {self.cliente.nome} - {self.produto.nome}"


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome
