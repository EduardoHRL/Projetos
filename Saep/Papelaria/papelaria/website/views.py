from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Livros
from .forms import *
from django.db.models import Sum
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

class LivroCreateView(CreateView):
    template_name = 'cadastrar_livro.html'
    model = Livros
    form_class = LivrosForm
    success_url = reverse_lazy('index')

class AutorCreateView(CreateView):
    template_name = 'cadastrar_autor.html'
    model = Autores
    form_class = AutoresForm
    success_url = reverse_lazy('index')

class EstoqueEntrada(ListView):
    template_name = 'estoque_entrada.html'
    model = Compras
    context_object_name = 'estoque_entrada'

class Comprar(CreateView):
    template_name = 'cadastrar_entrada.html'
    model = Compras
    form_class = ComprasForm
    success_url = reverse_lazy('estoque_entrada')

class EstoqueSaida(ListView):
    template_name = 'estoque_saida.html'
    model = Vendas
    context_object_name = 'estoque_saida'

class Vender(CreateView):
    template_name = 'vender_estoque.html'
    model = Vendas
    form_class = VendasForm
    success_url = reverse_lazy('estoque_saida')

class EstoqueAtualView(TemplateView):
    template_name = 'estoque_atual.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        entradas = Compras.objects.values(
            'livro_comprado__titulo', 
            'livro_comprado__preco'
        ).annotate(total_entrada=Sum('quantidade'))

        saidas = Vendas.objects.values(
            'livro_vendido__titulo'
        ).annotate(total_saida=Sum('quantidade'))

        saidas_dict = {item['livro_vendido__titulo']: item['total_saida'] for item in saidas}
        
        estoque = []
        for entrada in entradas:
            titulo_livro = entrada['livro_comprado__titulo']
            preco = entrada['livro_comprado__preco']
            total_entrada = entrada['total_entrada']
            total_saida = saidas_dict.get(titulo_livro, 0)
            saldo = total_entrada - total_saida

            estoque.append({
                'titulo': titulo_livro,
                'quantidade': saldo,
                'preco': preco
            })

        context['estoque'] = estoque
        return context
