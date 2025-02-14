from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', views.logar, name='logar'),
    path('cadastro', views.cadastro, name='cadastro'),

    path('laboratorios/', views.LaboratoriosListView.as_view(), name='lista_laboratorios'),
    path('laboratorios/cadastrar', views.LaboratoriosCreateView.as_view(), name='cadastra_laboratorios'),
    path('laboratorios/excluir/<int:pk>', views.LaboratoriosDeleteView.as_view(), name='exclui_laboratorios'),
    path('laboratorios/<int:pk>', views.LaboratoriosUpdateView.as_view(), name='atualiza')
]