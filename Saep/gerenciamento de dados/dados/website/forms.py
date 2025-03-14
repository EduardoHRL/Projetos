from django import forms
from .models import *

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes

        nome = forms.CharField(max_length=100, required=True, label='Nome')
        email = forms.EmailField(max_length=255, required=True, label='Email')
        nome = forms.IntegerField(required=True, label='Telefone')

        fields = [
            'nome',
            'email',
            'telefone'
        ]

class ClienteSearchForm(forms.Form):
    nome = forms.CharField(required=False, label="Nome")
    email = forms.CharField(required=False, label="Email")

class PedidosForm(forms.ModelForm):
    data_pedido = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Pedidos
        fields = ['cliente', 'produto', 'data_pedido']