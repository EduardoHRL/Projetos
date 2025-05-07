from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('usuarios/', UsuariosCreateView.as_view(), name='cadastrar_usuario'),

    path('tarefas/', TarefasListView.as_view(), name='lista_tarefas'),
    path('tarefas/cadastrar/', TarefasCreateView.as_view(), name='cadastrar_tarefas'),
    path('tarefas/atualizar/<int:pk>/', TarefasUpdateView.as_view(), name='atualizar_tarefa'),
    path('tarefas/deletar/<int:pk>/', TarefasDeleteView.as_view(), name='deletar_tarefa'),
    path('tarefas/atualiza_status/<int:pk>/', atualizar_status, name='atualiza_status')
]