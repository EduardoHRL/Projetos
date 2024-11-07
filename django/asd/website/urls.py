# website/urls.py
from django.urls import path
from .views import (
    index,
    FuncionarioListView,
    FuncionarioUpdateView,
    FuncionarioDeleteView,
    FuncionarioCreateView,
)

app_name = 'website'  # Defina o namespace do aplicativo

urlpatterns = [
    path('', index, name='index'),  # URL da página inicial
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
]
