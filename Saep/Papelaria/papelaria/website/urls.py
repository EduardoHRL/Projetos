from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('cadastrar_livro/', views.LivroCreateView.as_view(), name='cadastrar_livro'),

    path('cadastrar_autor/', views.AutorCreateView.as_view(), name='cadastrar_autor'),

    path('estoque/compras/', views.EstoqueEntrada.as_view(), name='estoque_entrada'),
    path('estoque/comprar', views.Comprar.as_view(), name='cadastrar_entrada'),

    path('estoque/vendas', views.EstoqueSaida.as_view(), name='estoque_saida'),
    path('estoque/vender', views.Vender.as_view(), name='vender_estoque'),

    path('estoque_atual/', views.EstoqueAtualView.as_view(), name='estoque_atual'),
]