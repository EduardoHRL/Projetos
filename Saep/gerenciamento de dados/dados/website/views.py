from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from website.forms import ClientesForm, PedidosForm
from .models import Clientes, Produtos, Pedidos

def index(request):
    return render(request, 'index.html')

class ClienteListView(ListView):
    model = Clientes
    template_name = 'lista_clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset = Clientes.objects.all()
        query_nome = self.request.GET.get('nome')
        query_email = self.request.GET.get('email')

        if query_nome:
            queryset = queryset.filter(nome__icontains=query_nome)
        if query_email:
            queryset = queryset.filter(email__icontains=query_email)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['email'] = self.request.GET.get('email', '')
        return context

class ClienteCreateView(CreateView):
    model = Clientes
    template_name = 'cadastra_cliente.html'
    form_class = ClientesForm
    success_url = reverse_lazy('lista_clientes')

class ClienteUpdateView(UpdateView):
    model = Clientes
    template_name = 'atualiza_cliente.html'
    fields = ['nome', 'email', 'telefone']
    success_url = reverse_lazy('lista_clientes')

class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'deleta_cliente.html'
    success_url = reverse_lazy('lista_clientes')


class ProdutoListView(ListView):
    model = Produtos
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        queryset = Produtos.objects.all()
        query_nome = self.request.GET.get('nome')
        query_preco = self.request.GET.get('preco')

        if query_nome:
            queryset = queryset.filter(nome__icontains=query_nome)
        if query_preco:
            queryset = queryset.filter(preco__gte=query_preco)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = self.request.GET.get('nome', '')
        context['preco'] = self.request.GET.get('preco', '')
        return context

class ProdutoCreateView(CreateView):
    model = Produtos
    template_name = 'cadastra_produto.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('lista_produtos')

class ProdutoUpdateView(UpdateView):
    model = Produtos
    template_name = 'atualiza_produto.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('lista_produtos')

class ProdutoDeleteView(DeleteView):
    model = Produtos
    template_name = 'deleta_produto.html'
    success_url = reverse_lazy('lista_produtos')


class PedidoListView(ListView):
    model = Pedidos
    template_name = 'lista_pedidos.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        queryset = Pedidos.objects.all()
        query_cliente = self.request.GET.get('cliente')
        query_produto = self.request.GET.get('produto')

        if query_cliente:
            queryset = queryset.filter(cliente__nome__icontains=query_cliente)
        if query_produto:
            queryset = queryset.filter(produto__nome__icontains=query_produto)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = self.request.GET.get('cliente', '')
        context['produto'] = self.request.GET.get('produto', '')
        return context

class PedidoCreateView(CreateView):
    model = Pedidos
    template_name = 'cadastra_produto.html'
    form_class = PedidosForm
    success_url = reverse_lazy('lista_pedidos')

class PedidoUpdateView(UpdateView):
    model = Pedidos
    template_name = 'atualiza_pedido.html'
    fields = ['cliente', 'produto', 'data_pedido']
    success_url = reverse_lazy('lista_pedidos')

class PedidoDeleteView(DeleteView):
    model = Pedidos
    template_name = 'deleta_pedido.html'
    success_url = reverse_lazy('lista_pedidos')