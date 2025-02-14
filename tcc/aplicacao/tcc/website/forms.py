from django import forms
from .models import Laboratorios, Usuarios

class LaboratoriosForm(forms.ModelForm):
    class Meta:
        model = Laboratorios
        fields = [
            'lab_nome',
            'lab_descricao',
            'lab_capacidade',
            'lab_status'
        ]

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            'usu_nome',
            'usu_email',
            'usu_cpf',
            'usu_telefone',
            'usu_tipoUsuario',
            'usu_senha'
        ]

        widgets = {
            'usu_senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
        }