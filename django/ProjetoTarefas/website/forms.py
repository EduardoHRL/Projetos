from django import forms
from website.models import *

class InsereUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'nome',
            'email'
        ]
        exclude = []

class InsereTarefaForm(forms.ModelForm):
    Opcoes = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta'),
    ]
    Op = [
        ('Pendente', 'Pendente'),
    ]

    prioridade = forms.ChoiceField(choices=Opcoes, widget=forms.Select(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Op,widget=forms.Select(attrs={'class': 'form-control'}))  

    class Meta:
        model = Tarefa

        fields = [
            'descricao',
            'setor',
            'prioridade',
            'usuario',
            'data',
            'status'
        ]

        exclude = []