from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'index.html')

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Administradores').exists():
                return HttpResponseRedirect(reverse('lista_cursos'))
            else:
                return HttpResponseRedirect(reverse('index')) 
        else:
            messages.error(request, 'Usuário e/ou senha estão incorretos.')

    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        is_admin = request.POST.get('is_admin') == 'on'

        if Aluno.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error': 'Este e-mail já está em uso.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'error': 'Nome de usuário já existe.'})

        user = User.objects.create_user(username=username, password=password)
        
        Aluno.objects.create(
            user=user,
            nome=nome,
            email=email,
            telefone=telefone,
            is_admin=is_admin
        )
        
        login(request, user)
        return redirect('index')
    
    return render(request, 'cadastro.html')


class CursoListView(LoginRequiredMixin, ListView):
    template_name = 'cursos/lista.html'
    model = Curso
    context_object_name = 'cursos'

    def get_queryset(self):
        queryset = Curso.objects.all()
        query_nome = self.request.GET.get('nome')
        query_instrutor = self.request.GET.get('instrutor')

        if query_nome:
            queryset = queryset.filter(nome__icontains=query_nome)
        if query_instrutor:
            queryset = queryset.filter(instrutor__icontains=query_instrutor)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['instrutor'] = self.request.GET.get('instrutor', '')
        return context

class CursoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'cursos/criar.html'
    model = Curso
    form_class = CursoForm
    success_url = reverse_lazy('lista_cursos')
    
    def test_func(self):
        return self.request.user.aluno.is_admin

class CursoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'cursos/atualizar.html'
    model = Curso
    form_class = CursoForm
    success_url = reverse_lazy('lista_cursos')
    
    def test_func(self):
        return self.request.user.aluno.is_admin

class CursoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'cursos/deletar.html'
    model = Curso
    success_url = reverse_lazy('lista_cursos')
    
    def test_func(self):
        return self.request.user.aluno.is_admin


class AlunoListView(LoginRequiredMixin, ListView):
    template_name = 'alunos/lista.html'
    model = Aluno
    context_object_name = 'alunos'

    def get_queryset(self):
        queryset = Aluno.objects.all()
        query_nome = self.request.GET.get('nome')
        query_email = self.request.GET.get('email')

        if query_nome:
            queryset = queryset.filter(nome__icontains=query_nome)
        if query_email:
            queryset = queryset.filter(email__icontains=query_email)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['email'] = self.request.GET.get('email', '')
        return context
    

class AlunoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'alunos/atualizar.html'
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('lista_alunos')
    
    def test_func(self):
        return self.request.user.aluno.is_admin

class AlunoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'alunos/deletar.html'
    model = Aluno
    success_url = reverse_lazy('lista_alunos')
    
    def test_func(self):
        return self.request.user.aluno.is_admin


class InscricaoListView(LoginRequiredMixin, ListView):
    template_name = 'inscricoes/lista.html'
    model = Inscricao
    context_object_name = 'inscricoes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluno'] = self.request.GET.get('aluno', '')
        context['curso'] = self.request.GET.get('curso', '')
        return context

class InscricaoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'inscricoes/criar.html'
    model = Inscricao
    form_class = InscricaoForm
    success_url = reverse_lazy('lista_inscricoes')

    def form_valid(self, form):
        form.instance.aluno = Aluno.objects.get(user=self.request.user)
        return super().form_valid(form)

class InscricaoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inscricoes/deletar.html'
    model = Inscricao
    success_url = reverse_lazy('lista_inscricoes')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(aluno__user=self.request.user)