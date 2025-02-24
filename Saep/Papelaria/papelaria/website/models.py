from django.db import models


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'autores'

    def __str__(self):
        return self.nome


class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    livro_comprado = models.ForeignKey('Livros', on_delete=models.CASCADE, db_column='livro_comprado', blank=True, null=True, related_name='compras')
    quantidade = models.IntegerField(blank=True, null=True)
    data_compra = models.DateTimeField(blank=True, null=True, auto_now_add= True)

    class Meta:
        db_table = 'compras'

    def __str__(self):
        return self.livro_comprado


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True, null=True)
    edicao = models.CharField(max_length=45, blank=True, null=True)
    editora = models.CharField(max_length=100, blank=True, null=True)
    ano_publicacao = models.IntegerField(blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)
    categoria = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'livros'

    def __str__(self):
        return self.titulo


class LivrosAutores(models.Model):
    livro = models.OneToOneField(Livros, on_delete=models.CASCADE, primary_key=True)  # The composite primary key (livro_id, autor_id) found, that is not supported. The first column is selected.
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)

    class Meta:
        db_table = 'livros_autores'
        unique_together = (('livro', 'autor'),)


class Vendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    livro_vendido = models.ForeignKey(Livros, on_delete=models.CASCADE, db_column='livro_vendido', blank=True, null=True, related_name='vendas')
    quantidade = models.IntegerField(blank=True, null=True)
    data_venda = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        db_table = 'vendas'
