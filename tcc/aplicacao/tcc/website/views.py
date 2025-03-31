from .models import Laboratorios, Usuarios, Escola
from .forms import LaboratoriosForm, UsuariosForm, EscolaForm
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')

def lab(request):
    return render(request, 'laboratorios.html')

def logar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuarios.objects.get(usu_email = email)
        except Usuarios.DoesNotExist:
            messages.error(request, 'Email e/ou senha estão incorretos')
            return redirect('logar')
            
        if check_password(senha, usuario.usu_senha):
            request.session['usuario_id'] = usuario.usu_codigo
            request.session['usuario_nome'] = usuario.usu_nome
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Email e/ou senha estão incorretos')
        
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        tipoUsuario = request.POST.get('tipoUsuario')
        senha = request.POST.get('senha')

        if Usuarios.objects.filter(usu_email=email).exists() or Usuarios.objects.filter(usu_cpf=cpf).exists():
            if Usuarios.objects.filter(usu_email=email).exists():
                messages.error(request, 'Email já existe.')
            if Usuarios.objects.filter(usu_cpf=cpf).exists():
                messages.error(request, 'Cpf já existe.')
            return redirect('cadastro')

        usuarios = Usuarios.objects.create(
            usu_nome = nome,
            usu_email = email,
            usu_cpf = cpf,
            usu_telefone = telefone,
            usu_tipoUsuario = tipoUsuario,
            usu_senha = make_password(senha)
        )

        messages.success(request, 'Cadastro realizado com sucesso')
        return HttpResponseRedirect(reverse('logar'))

    return render(request, 'cadastro.html')
    
def logout(request):
    request.session.flush()
    messages.info(request, 'Tenha um bom dia!')
    return redirect('logar')


class UsuariosListView(LoginRequiredMixin, ListView):
    template_name = 'lista_usuarios.html'
    model = Usuarios
    context_object_name = 'usuarios'

class UsuariosCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cadastro_usuarios.html'
    model = Usuarios
    form_class = UsuariosForm
    success_url = reverse_lazy('lista_usuarios')

class UsuariosUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'atualiza_usuarios.html'
    model = Usuarios
    form_class = UsuariosForm
    success_url = reverse_lazy('lista_usuarios')

class UsuariosDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'deleta_usuarios.html'
    model = Usuarios
    success_url = reverse_lazy('lista_usuarios')

class LaboratoriosListView(LoginRequiredMixin, ListView):
    template_name = 'lista_laboratorios.html'
    model = Laboratorios
    context_object_name = 'laboratorios'

class LaboratoriosCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cadastro_laboratorios.html'
    model = Laboratorios
    form_class = LaboratoriosForm
    success_url = reverse_lazy('lista_laboratorios')
    
class LaboratoriosUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'atualiza_laboratorios.html'
    model = Laboratorios
    form_class = LaboratoriosForm
    success_url = reverse_lazy('lista_laboratorios')
    
class LaboratoriosDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'exclui_laboratorios.html'
    model = Laboratorios
    success_url = reverse_lazy('lista_laboratorios')