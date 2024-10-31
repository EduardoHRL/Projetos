from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from sistema.models import tbl_usuarios
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django import forms

class InsereUsuarioForm(forms.ModelForm):
    class Meta:
        model = tbl_usuarios

        field = [
            'nome',
            'username',
            'senha'
        ]

class ListaUsuarios(ListView):
    template_name= "templates/usuarios.html"
    model = tbl_usuarios
    context_object_name = 'usuarios'

def cria_usuario(request, pk):
    #Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuarios'))
        
    else:
        return render(request, "templates/form.html", {'form': form})
    
class UsuarioListView(UpdateView):
    template_name = "web/lista.html"
    model = tbl_usuarios
    context_object_name = 'usuarios'

class UsuarioUpdateView(ListView):
    template_name = "atualiza.html"
    model = tbl_usuarios
    field = '__all__'
    context_object_name = 'usuarios'

    def get_object(self, queryset = None):
        usuario = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            usuario = tbl_usuarios.objects.filter(id=id).first()

        return usuario
    
class UsuarioDeleteView(DeleteView):
    template_name = "web/exclui.html"
    model = tbl_usuarios
    context_object_name = 'usuarios'
    success_url = reverse_lazy(
        "website:lista_usuarios"
    )

class UsuarioCreateView(CreateView):
    template_name = "web/cria.html"
    model = tbl_usuarios
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("web:lista_usuarios")


