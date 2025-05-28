from django import forms
from .models import *
from django.forms import inlineformset_factory, modelformset_factory
from django.db.models import Q
from django.utils import timezone
from datetime import datetime

class LaboratoriosForm(forms.ModelForm):
    lab_nome = forms.CharField(
        label="Nome do Laboratório",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    lab_capacidade = forms.IntegerField(
        label="Capacidade",
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    lab_status = forms.ChoiceField(
        choices=Laboratorios.STATUS_ESCOLHA,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    lab_descricao = forms.CharField(
        label="Descrição",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    lab_foto = forms.ImageField(
        label="Foto",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Laboratorios
        fields = [
            'lab_nome',
            'lab_descricao',
            'lab_capacidade',
            'lab_status',
            'lab_foto',
        ]

HorarioLaboratorioFormset = modelformset_factory(
    Disponibilidade,
    fields=('hor_inicio', 'hor_fim', 'hor_diasDisponiveis'),
    extra=1,
)


class LaboratorioEquipamentoForm(forms.ModelForm):
    class Meta:
        model = LaboratorioEquipamento
        fields = [
            'equipamento',
            'quantidade'
        ]

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios

        fields = '__all__'

class ReservasForm(forms.ModelForm):
    res_dia_semana = forms.MultipleChoiceField(
        choices=DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple(attrs={'class': "inline-block mr-3"}),
        required=False
    )

    class Meta:
        model = Reservas
        fields = [
            'laboratorio',
            'res_inicio',
            'res_fim',
            'res_repeticao',
            'res_intervalo_semanas',
            'res_dia_semana',
            'res_data_final_repeticao',
            'res_descricao'
        ]

        widgets = {
            "laboratorio": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "res_inicio": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "w-full border rounded p-2"}, format="%Y-%m-%dT%H:%M"
),
            "res_fim": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "w-full border rounded p-2"}, format="%Y-%m-%dT%H:%M"
),
            "res_repeticao": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "res_intervalo_semanas": forms.NumberInput(attrs={"class": "w-full border rounded p-2"}),
            "res_data_final_repeticao": forms.DateInput(attrs={"type": "date", "class": "w-full border rounded p-2"}),
            "res_descricao": forms.Textarea(attrs={"class": "w-full border rounded p-2", "rows": 3}),
        }

    def clean_res_inicio(self):
        data = self.cleaned_data.get('res_inicio')
        if isinstance(data, str):
            try:
                # Formato: "YYYY-MM-DD HH:MM"
                return datetime.strptime(data, '%Y-%m-%d %H:%M')
            except ValueError:
                # Formato alternativo para edição: "YYYY-MM-DDTHH:MM"
                return datetime.strptime(data, '%Y-%m-%dT%H:%M')
        return data

    def clean_res_fim(self):
        data = self.cleaned_data.get('res_fim')
        if isinstance(data, str):
            try:
                return datetime.strptime(data, '%Y-%m-%d %H:%M')
            except ValueError:
                return datetime.strptime(data, '%Y-%m-%dT%H:%M')
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        repeticao = cleaned_data.get('res_repeticao')

        if repeticao == 'S':
            if not cleaned_data.get("res_intervalo_semanas"):
                self.add_error("res_intervalo_semanas", "Campo obrigatório para repetição semanal.")
            if cleaned_data.get("res_dia_semana") is None:
                self.add_error("res_dia_semana", "Informe o dia da semana.")
            if not cleaned_data.get("res_data_final_repeticao"):
                self.add_error("res_data_final_repeticao", "Informe a data final da repetição.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].queryset = Laboratorios.objects.filter(lab_status='disponivel')
        self.fields['res_inicio'].required = False
        self.fields['res_fim'].required    = False

class AtualizarReservasForm(forms.ModelForm):
    res_dia_semana = forms.MultipleChoiceField(
        choices=DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple(attrs={'class': "inline-block mr-3"}),
        required=False
    )

    class Meta:
        model = Reservas
        fields = [
            'laboratorio',
            'res_inicio',
            'res_fim',
            'res_repeticao',
            'res_intervalo_semanas',
            'res_dia_semana',
            'res_data_final_repeticao',
            'res_descricao'
        ]

        widgets = {
            "laboratorio": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "res_inicio": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "w-full border rounded p-2"},
                format="%Y-%m-%dT%H:%M"
            ),
            "res_fim": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "w-full border rounded p-2"},
                format="%Y-%m-%dT%H:%M"
            ),
            "res_repeticao": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "res_intervalo_semanas": forms.NumberInput(attrs={"class": "w-full border rounded p-2"}),
            "res_data_final_repeticao": forms.DateInput(
                attrs={"type": "date", "class": "w-full border rounded p-2"},
                format="%Y-%m-%d"
            ),
            "res_descricao": forms.Textarea(attrs={"class": "w-full border rounded p-2", "rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        repeticao = cleaned_data.get('res_repeticao')

        if repeticao == 'S':
            if not cleaned_data.get("res_intervalo_semanas"):
                self.add_error("res_intervalo_semanas", "Campo obrigatório para repetição semanal.")
            if not cleaned_data.get("res_dia_semana"):
                self.add_error("res_dia_semana", "Informe o dia da semana.")
            if not cleaned_data.get("res_data_final_repeticao"):
                self.add_error("res_data_final_repeticao", "Informe a data final da repetição.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.laboratorio:
            lab_atual = self.instance.laboratorio
            self.fields['laboratorio'].queryset = Laboratorios.objects.filter(
                Q(lab_status='disponivel') | Q(pk=lab_atual.pk)
            )
        else:
            self.fields['laboratorio'].queryset = Laboratorios.objects.filter(lab_status='disponivel')

        if self.instance.res_inicio:
            self.fields['res_inicio'].initial = self.instance.res_inicio.strftime('%Y-%m-%dT%H:%M')
        if self.instance.res_fim:
            self.fields['res_fim'].initial = self.instance.res_fim.strftime('%Y-%m-%dT%H:%M')
        if self.instance.res_data_final_repeticao:
            self.fields['res_data_final_repeticao'].initial = self.instance.res_data_final_repeticao.strftime('%Y-%m-%d')

        self.fields['res_dia_semana'].initial = self.instance.res_dia_semana

class EscolaForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'logo', 'cep', 'cidade', 'estado', 'endereco', 'telefone', 'email', 'horario_inicio', 'horario_fim', 'bairro']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded p-2 w-80'}),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'accept': 'image/jpeg, image/png',
                'id': 'logo-input'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'border rounded p-2 w-80',
                'x-model': 'cep',
                '@input': 'formatarCep($event.target)',
                '@blur': 'buscarCep($event.target)',
                'minlength': '9',
                'maxlength': '9',
                'placeholder': '00000-000'
            }),
            'cidade': forms.TextInput(attrs={'class': 'border rounded p-2 w-80', 'x-model': 'cidade', 'readonly': True}),
            'estado': forms.TextInput(attrs={'class': 'border rounded p-2 w-80', 'x-model': 'estado', 'readonly': True}),
            'endereco': forms.TextInput(attrs={'class': 'border rounded p-2 w-80'}),
            'bairro': forms.TextInput(attrs={'class': 'border rounded p-2 w-80'}),
            'telefone': forms.TextInput(attrs={'class': 'border rounded p-2 w-80'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded p-2 w-80'}),
            'horario_inicio': forms.TimeInput(attrs={'class': 'border rounded p-2 w-80', 'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'class': 'border rounded p-2 w-80', 'type': 'time'})
        }
        labels = {
            'horario_inicio': 'Horário de abertura',
            'horario_fim': 'Horário de fechamento',
            'endereco': 'Endereço'
        }
