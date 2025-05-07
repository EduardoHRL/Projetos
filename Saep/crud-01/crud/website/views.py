from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

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

def atualizar_status(request, pk):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        tarefa = get_object_or_404(Tarefas, id=pk)
        tarefa.status = novo_status
        tarefa.save()
        return HttpResponseRedirect(reverse('lista_tarefas'))
