from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('cadastra_usuario/', views.UsuarioCreateView.as_view(), name='cadastra_usuario'),

    path('cadastra_tarefa/', views.TarefaCreateView.as_view(), name='cadastra_tarefa'),

    path('tarefas/', views.TarefaListView.as_view(), name='lista_tarefas'),

    path('tarefas/atualiza/<int:pk>', views.TarefaUpdateView.as_view(), name='atualiza_tarefa'),

    path('tarefas/deleta/<int:pk>/', views.TarefaDeleteView.as_view(), name='deleta_tarefa'),

    path('tarefas/atualiza_status/<int:pk>/', views.atualiza_status, name='atualiza_status'),
]