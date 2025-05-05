from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import *
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from website.forms import AlunoForm, CursoForm, InscricaoForm
from .models import *
from django.utils.decorators import method_decorator

@login_required
def index(request):
    return render(request, 'index.html')

class AlunosListView(ListView):
    template_name = 'lista_alunos.html'
    model = Alunos
    context_object_name = 'alunos'

    def get_queryset(self):
        queryset = Alunos.objects.all()
        query_nome = self.request.GET.get('nome')
        query_email = self.request.GET.get('email')

        if query_nome:
            queryset = queryset.filter(username__icontains=query_nome)
        if query_email:
            queryset = queryset.filter(email__icontains=query_email)
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['email'] = self.request.GET.get('email', '')
        return context
    
class LoginView(AuthLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')

class CadastroView(CreateView):
    model = Alunos
    form_class = AlunoForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('lista_alunos')

class AlunosUpdateView(UpdateView):
    model = Alunos
    form_class = AlunoForm
    template_name = 'atualizar_aluno.html'
    success_url = reverse_lazy('lista_alunos')

class AlunosDeleteView(DeleteView):
    template_name = 'deletar_aluno.html'
    model = Alunos
    success_url = reverse_lazy('lista_alunos')    

class CursosListView(ListView):
    template_name = 'cursos/lista.html'
    model = Cursos
    context_object_name = 'cursos'

    def get_queryset(self):
        queryset = Cursos.objects.all()
        query_nome = self.request.GET.get('nome')
        query_instrutor = self.request.GET.get('instrutor')

        if query_nome:
            queryset = queryset.filter(nome__icontains=query_nome)
        if query_instrutor:
            queryset = queryset.filter(instrutor__icontains=query_instrutor)
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['instrutor'] = self.request.GET.get('instrutor', '')
        return context

class CursosCreateView(CreateView):
    template_name = 'cursos/criar.html'
    model = Cursos
    form_class = CursoForm
    success_url = reverse_lazy('lista_cursos')

class CursosUpdateView(UpdateView):
    template_name = 'cursos/atualizar.html'
    model = Cursos
    form_class = CursoForm
    success_url = reverse_lazy('lista_cursos')

class CursosDeleteView(DeleteView):
    template_name = 'cursos/deletar.html'
    model = Cursos
    success_url = reverse_lazy('lista_cursos')


class InscricaoListView(ListView):
    template_name = 'inscricao/lista.html'
    model = Inscricoes
    context_object_name = 'inscricoes'

    def get_queryset(self):
        queryset = Inscricoes.objects.all()
        query_aluno = self.request.GET.get('aluno')
        query_curso = self.request.GET.get('curso')

        if query_aluno:
            queryset = queryset.filter(aluno__username__icontains=query_aluno)
        if query_curso:
            queryset = queryset.filter(curso__nome__icontains=query_curso)
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['aluno'] = self.request.GET.get('aluno', '')
        context['curso'] = self.request.GET.get('curso', '')
        return context

class InscricaoCreateView(CreateView):
    template_name = 'inscricao/criar.html'
    model = Inscricoes
    form_class = InscricaoForm
    success_url = reverse_lazy('lista_inscricoes')


class InscricaoDeleteView(DeleteView):
    template_name = 'inscricao/deletar.html'
    model = Inscricoes
    success_url = reverse_lazy('lista_inscricoes')