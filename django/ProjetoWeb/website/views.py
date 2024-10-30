from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from cadastro.models import Funcionario
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from website.forms import InsereFuncionarioForm


class ListaFuncionarios(ListView):
    template_name = "templates/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"

def cria_funcionario(request, pk):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))
        
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})
    
class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            funcionario = Funcionario.objects.filter(id=id).first()

        # Retorna o objeto encontrado
        return funcionario
    

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
        "website:lista_funcionarios"
)
    
class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")


