from .models import TblUsuario, TblTarefas
from django import forms

class CadastraUsuarioForm(forms.ModelForm):
    usu_nome = forms.CharField(required=True, max_length=255, label='Nome')
    usu_email = forms.CharField(required=True, max_length=255, label='Email')

    class Meta:
        model = TblUsuario

        fields = [
            'usu_nome',
            'usu_email'
        ]

class CadastraTarefaForm(forms.ModelForm):
    opcoes = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta')
    ]

    tar_prioridade = forms.ChoiceField(choices=opcoes, widget=forms.Select, label='Prioridade', required=True)
    tar_descricao = forms.CharField(required=True, max_length=255)
    class Meta:
        model = TblTarefas

        fields = [
            'tar_descricao',
            'tar_nomesetor',
            'usu',
            'tar_prioridade'
        ]

        labels = {
            'tar_descricao': 'Descrição',
            'tar_nomesetor': 'Nome do Setor',
            'usu': 'Usuário'
        }