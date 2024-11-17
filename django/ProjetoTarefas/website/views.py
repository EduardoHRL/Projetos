
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse, reverse_lazy
from website.models import *
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from website.forms import *

def index(request):
    return render(request, 'index.html')

def usuarios(request):

    usuarios = Usuario.objects.all()

    contexto = {'usuarios': usuarios}

    return render(request, 'usuarios.html', contexto)

def cria_usuario(request):
    form = request.POST.get.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('lista_usuarios'))

    return render(request, 'form_usuario.html', {'form_usuario': form})

def tarefas(request):

    tarefas = Tarefa.objects.all()

    contexto = {'tarefas': tarefas}

    return render(request, 'tarefas.html', contexto)

def cria_tarefa(request):
    form = request.POST.get.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('lista_tarefas'))
    
    return render(request, 'form_tarefa.html', {'form_tarefa': form})

class UsuarioListView(ListView):
    template_name = 'lista_usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    template_name = 'cadastra_usuario.html'
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy('lista_usuarios')

class UsuarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuarios'

    def get_object(self):
        usuario = None

        id = self.kwargs.get(self.pk_url_kwarg)
        if id is not None:
            usuario = Usuario.objects.filter(usu_codigo=id).first()
        return usuario
    
    success_url = reverse_lazy('lista_usuarios')

class UsuarioDeleteView(DeleteView):
    template_name = 'exclui_usuario.html'
    model = Usuario
    content_object_name = 'usuarios'
    success_url = reverse_lazy('lista_usuarios')


class TarefaListView(ListView):
    template_name = 'lista_tarefas.html'
    model = Tarefa
    context_object_name = 'tarefas'

class TarefaCreateView(CreateView):
    template_name = 'cadastra_tarefa.html'
    model = Tarefa
    form_class = InsereTarefaForm
    success_url = reverse_lazy('lista_tarefas')

class TarefaDeleteView(DeleteView):
    template_name = 'exclui_tarefa.html'
    model = Tarefa
    context_object_name = 'usuarios'
    success_url = reverse_lazy('lista_tarefas')

def atualiza_status(request, pk):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        tarefa = Tarefa.objects.filter(tar_codigo=pk).first()
        tarefa.status = novo_status
        tarefa.save()
        return HttpResponseRedirect(reverse('lista_tarefas'))


