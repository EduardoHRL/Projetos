from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

class UsuariosCreateView(CreateView):
    template_name = 'usuarios/criar.html'
    model = Usuarios
    form_class = UsuariosForm
    success_url = reverse_lazy('index')

class TarefasListView(ListView):
    template_name = 'tarefas/lista.html'
    model = Tarefas
    context_object_name = 'tarefas'

class TarefasCreateView(CreateView):
    template_name = 'tarefas/criar.html'
    model = Tarefas
    form_class = TarefasForm
    success_url = reverse_lazy('lista_tarefas')

class TarefasUpdateView(UpdateView):
    template_name = 'tarefas/criar.html'
    model = Tarefas
    form_class = TarefasForm
    success_url = reverse_lazy('lista_tarefas')

class TarefasDeleteView(DeleteView):
    template_name = 'tarefas/deletar.html'
    model = Tarefas
    success_url = reverse_lazy('lista_tarefas')
