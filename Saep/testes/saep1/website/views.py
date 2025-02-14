from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import TblTarefas, TblUsuario
from .forms import CadastraUsuarioForm, CadastraTarefaForm

def index(request):
    return render(request, 'index.html')

class UsuarioCreateView(CreateView):
    template_name = 'cadastra_usuario.html'
    model = TblUsuario
    form_class = CadastraUsuarioForm
    success_url = reverse_lazy('index')

class TarefaCreateView(CreateView):
    template_name = 'cadastra_tarefa.html'
    model = TblTarefas
    form_class = CadastraTarefaForm
    success_url = reverse_lazy('index')
