from django import forms
from .models import *
    
class UsuariosForm(forms.ModelForm):
    nome = forms.CharField(label='Nome',required=True,)
    class Meta:
        model = Usuarios

        fields = [
            'nome',
            'email'
        ]

class TarefasForm(forms.ModelForm):
    prioridade_escolha = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta')
    ]

    descricao = forms.CharField(label='Descrição', required=True,
                                widget=forms.TextInput(attrs={'class': 'resize-none'}))
    
    prioridade = forms.ChoiceField(label='Prioridade', required=True,
                                   widget=forms.Select(), choices=prioridade_escolha)
    class Meta:
        model = Tarefas
        
        fields = [
            'descricao',
            'nome_setor',
            'prioridade',
            'usuarios'
        ]