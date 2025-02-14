from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('cadastra_usuario/', views.UsuarioCreateView.as_view(), name='cadastra_usuario'),

    path('cadastra_tarefa/', views.TarefaCreateView.as_view(), name='cadastra_tarefa')
]