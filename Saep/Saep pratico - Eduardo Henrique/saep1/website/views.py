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
    success_url = reverse_lazy('lista_tarefas')

class TarefaListView(ListView):
    template_name = 'lista_tarefas.html'
    model = TblTarefas
    context_object_name = 'tarefas'

class TarefaUpdateView(UpdateView):
    template_name = 'atualiza_tarefa.html'
    model = TblTarefas
    form_class = CadastraTarefaForm
    success_url = reverse_lazy('lista_tarefas')

class TarefaDeleteView(DeleteView):
    template_name = 'deleta_tarefa.html'
    model = TblTarefas
    success_url = reverse_lazy('lista_tarefas')

def atualiza_status(request, pk):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        tarefa = TblTarefas.objects.filter(tar_id=pk).first()
        tarefa.tar_status = novo_status
        tarefa.save()
        return HttpResponseRedirect(reverse('lista_tarefas'))


