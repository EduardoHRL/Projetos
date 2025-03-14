from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('cliente/cadastro/', views.ClienteCreateView.as_view(), name='cadastra_cliente'),
    path('cliente/<int:pk>/atualizar/', views.ClienteUpdateView.as_view(), name='atualiza_cliente'),
    path('cliente/<int:pk>/deletar/', views.ClienteDeleteView.as_view(), name='deleta_cliente'),

    path('produtos/', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('produto/cadastro/', views.ProdutoCreateView.as_view(), name='cadastra_produto'),
    path('produto/<int:pk>/atualizar/', views.ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produto/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='deleta_produto'),

    path('pedidos/', views.PedidoListView.as_view(), name='lista_pedidos'),
    path('pedido/cadastro/', views.PedidoCreateView.as_view(), name='cadastra_pedido'),
    path('pedido/<int:pk>/atualizar/', views.PedidoUpdateView.as_view(), name='atualiza_pedido'),
    path('pedido/<int:pk>/deletar', views.PedidoDeleteView.as_view(), name='deleta_pedido')
]
