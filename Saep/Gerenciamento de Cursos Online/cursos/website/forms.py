from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = [
            'nome',
            'descricao',
            'carga_horaria',
            'instrutor'
        ]

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno

        fields = [
            'nome',
            'email',
            'telefone',
        ]


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao

        fields = [
            'aluno',
            'curso'
        ]

