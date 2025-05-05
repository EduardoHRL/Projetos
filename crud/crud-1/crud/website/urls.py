from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('aluno/', AlunosListView.as_view(), name='lista_alunos'),
    path('aluno/atualizar/<int:pk>/', AlunosUpdateView.as_view(), name='atualizar_aluno'),
    path('aluno/deletar/<int:pk>/', AlunosDeleteView.as_view(), name='deletar_aluno'),

    path('curso/', CursosListView.as_view(), name='lista_cursos'),
    path('curso/criar/', CursosCreateView.as_view(), name='criar_curso'),
    path('curso/atualizar/<int:pk>/', CursosUpdateView.as_view(), name='atualizar_curso'),
    path('curso/deletar/<int:pk>/', CursosDeleteView.as_view(), name='deletar_curso'),

    path('inscricao/', InscricaoListView.as_view(), name='lista_inscricoes'),
    path('inscricao/criar/', InscricaoCreateView.as_view(), name='criar_inscricao'),
    path('inscricao/deletar/<int:pk>/', InscricaoDeleteView.as_view(), name='deletar_inscricao'),
]