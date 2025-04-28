import django_filters
from .models import *
from django import forms

class LaboratorioFilter(django_filters.FilterSet):
    lab_nome = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Filtrar por Nome'
    )

    class Meta:
        model = Laboratorios
        fields = [
            'lab_nome'
        ]