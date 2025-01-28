from django.contrib import admin
from django.urls import include, path
from website import views

urlpatterns = [
    path('', views.index, name='index'),

    path('funcionarios/', views.FuncionarioListView.as_view(), name='lista_funcionarios'),

    path('funcionario/<int:pk>',views.FuncionarioUpdateView.as_view(),name='atualiza_funcionario'),

    path('funcionario/excluir/<int:pk>',views.FuncionarioDeleteView.as_view(),name='deleta_funcionario'),

    path('funcionario/cadastrar/',views.FuncionarioCreateView.as_view(), name='cadastra_funcionario'),




]
