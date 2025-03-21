from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('login/', logar, name='login'),
    path('cadastro/', cadastro, name='cadastro'),

    path('cursos/', CursoListView.as_view(), name='lista_cursos'),
    path('cursos/criar/', CursoCreateView.as_view(), name='criar_curso'),
    path('cursos/<int:pk>/atualizar', CursoUpdateView.as_view(), name='atualiza_curso'),
    path('cursos/<int:pk>/deletar', CursoDeleteView.as_view(), name='deleta_curso'),

    path('alunos/', AlunoListView.as_view(), name='lista_alunos'),
    path('alunos/<int:pk>/atualizar', AlunoUpdateView.as_view(), name='atualiza_aluno'),
    path('alunos/<int:pk>/deletar', AlunoDeleteView.as_view(), name='deleta_aluno'),
    
    path('inscricoes/', InscricaoListView.as_view(), name='lista_inscricoes'),
    path('inscricoes/criar/', InscricaoCreateView.as_view(), name='criar_inscricao'),
    path('inscricoes/<int:pk>/deletar', InscricaoDeleteView.as_view(), name='deleta_inscricao'),
]