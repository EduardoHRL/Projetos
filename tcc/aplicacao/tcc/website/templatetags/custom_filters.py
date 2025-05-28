from django import template
import json
from django.template.defaultfilters import stringfilter
from ..models import DIAS_SEMANA, Laboratorios

register = template.Library()

@register.filter
@stringfilter
def format_dias_semana(value):
    dias_map = {
        '0': 'Segunda',
        '1': 'Terça',
        '2': 'Quarta',
        '3': 'Quinta',
        '4': 'Sexta',
        '5': 'Sábado',
        '6': 'Domingo'
    }
    dias = value.split(',')
    return ', '.join([dias_map.get(d.strip(), '') for d in dias])

@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key), '[]')

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def get_dia_nome(dia_num):
    return dict(DIAS_SEMANA).get(dia_num, '')

@register.filter
def laboratorio_nome(lab_id):
    try:
        return Laboratorios.objects.get(lab_codigo=lab_id).lab_nome
    except Laboratorios.DoesNotExist:
        return ""
    
