from django import forms
from django.contrib.auth.forms import UserCreationForm
from website.models import Alunos, Cursos, Inscricoes

class AlunoForm(UserCreationForm):
    class Meta:
        model = Alunos
        fields = [
            'username',
            'email',
            'telefone'
        ]

class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricoes
        fields = '__all__'