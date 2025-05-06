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
    descricao = forms.CharField(label='Descrição', required=True,
                                widget=forms.TextInput(attrs={'class': 'resize-none'}))
    class Meta:
        model = Tarefas
        
        fields = [
            'descricao',
            'nome_setor',
            'prioridade',
            'usuarios'
        ]