
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse, reverse_lazy
from website.models import *
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from website.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'Usuário e/ou senha estão incorretos.')

    return render(request, 'login.html')
        
def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request,'Usuário já existe.')
        else:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            return HttpResponseRedirect(reverse('logar'))

        
    return render(request, 'cadastro.html')
    
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

@login_required
def tarefas(request):

    tarefas = Tarefa.objects.filter(user=request.user)

    return render(request, 'tarefas.html', {'tarefas': tarefas})

def cria_tarefa(request):
    form = request.POST.get.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('lista_tarefas'))
    
    return render(request, 'form_tarefa.html', {'form_tarefa': form})

class UsuarioListView(LoginRequiredMixin, ListView):
    template_name = 'lista_usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'

class UsuarioCreateView(LoginRequiredMixin,CreateView):
    template_name = 'cadastra_usuario.html'
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy('lista_usuarios')

class UsuarioUpdateView(LoginRequiredMixin,UpdateView):
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

class UsuarioDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'exclui_usuario.html'
    model = Usuario
    content_object_name = 'usuarios'
    success_url = reverse_lazy('lista_usuarios')


class TarefaListView(LoginRequiredMixin,ListView):
    template_name = 'lista_tarefas.html'
    model = Tarefa
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

class TarefaCreateView(LoginRequiredMixin,CreateView):
    template_name = 'cadastra_tarefa.html'
    model = Tarefa
    form_class = InsereTarefaForm
    success_url = reverse_lazy('lista_tarefas')

class TarefaDeleteView(LoginRequiredMixin,DeleteView):
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


