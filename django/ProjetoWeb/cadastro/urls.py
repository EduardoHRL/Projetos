from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from website.views import FuncionarioListView
from website.views import FuncionarioUpdateView
from website.views import FuncionarioDeleteView
from website.views import FuncionarioCreateView


urlpatterns = [
    # Inclui as URLs do app website
    path('', include('website.urls', namespace='website')),

    # Interface administrativa
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name="index.html")),

    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),

    path('funcionario/<id>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),

    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),

    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),

]
