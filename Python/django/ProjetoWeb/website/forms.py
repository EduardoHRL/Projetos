from django import forms
from website.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
    # Modelo base
        model = Funcionario
# Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]
        # Campos que não estarão no form
        exclude = []
        