from django import forms
from .models import *

class LivrosForm(forms.ModelForm):
    Anos = [(ano, ano) for ano in range(2025, -1, -1)]

    titulo = forms.CharField(max_length=100, required=True, label='Título')
    isbn = forms.CharField(max_length=17, label='ISBN')
    edicao = forms.CharField(label='Edição')
    ano_publicacao = forms.ChoiceField(choices=Anos, label='Ano')
    preco = forms.FloatField(label='Preço(R$)', required=True)
    autores = forms.ModelMultipleChoiceField(queryset=Autores.objects.all(), widget=forms.CheckboxSelectMultiple, label='Autores')

    class Meta:

        model = Livros

        fields = [
            'titulo',
            'isbn',
            'edicao',
            'editora',
            'ano_publicacao',
            'preco',
            'categoria',
            'autores'
        ]

class AutoresForm(forms.ModelForm):
    nome = forms.CharField(max_length=255, required=True, label='Nome')

    class Meta:
        model = Autores

        fields = [
            'nome',
            'nacionalidade',
            'biografia'
        ]

class ComprasForm(forms.ModelForm):
    livro_comprado = forms.ModelChoiceField(queryset=Livros.objects.all(), widget=forms.Select, required=True, label='Livro')
    quantidade = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Compras

        fields = [
            'livro_comprado',
            'quantidade',

        ]

class VendasForm(forms.ModelForm):
    livro_vendido = forms.ModelChoiceField(queryset=Livros.objects.all(), widget=forms.Select, required=True, label='Livro')
    quantidade = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Vendas

        fields = [
            'livro_vendido',
            'quantidade'
        ]
