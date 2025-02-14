from .models import TblUsuario, TblTarefas
from django import forms

class CadastraUsuarioForm(forms.ModelForm):
    class Meta:
        model = TblUsuario

        fields = [
            'usu_nome',
            'usu_email'
        ]
        labels = {
            'usu_nome': 'Nome',
            'usu_email': 'Email'
        }

class CadastraTarefaForm(forms.ModelForm):
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
            'usu': 'Usuário',
            'tar_prioridade': 'Prioridade'
        }