from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from website.forms import InsereFuncionarioForm
from website.models import Funcionario

def index(request):
    return render(request, 'index.html')

def funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objetos.all()
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "funcionarios.html", contexto)

def cria_funcionario(request, pk):
    form = request.POST.get.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('lista_funcionarios'))
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "form.html", {'form': form})
    
class FuncionarioListView(ListView):
    template_name = "lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionarios'

    def get_object(self, queryset=None):
        funcionario = None
        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        if id is not None:
        # Busca o funcionario apartir do id
            funcionario = Funcionario.objetos.filter(id=id).first()
        return funcionario
    
    success_url = reverse_lazy('lista_funcionarios')
    
class FuncionarioDeleteView(DeleteView):
    template_name = "exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioCreateView(CreateView):
    template_name = "cadastra-funcionario.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("lista_funcionarios")



