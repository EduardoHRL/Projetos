from django.urls import include
from django.contrib import admin
from django.urls import path
from web.views import UsuarioListView
from web.views import UsuarioUpdateView
from web.views import UsuarioDeleteView
from web.views import UsuarioCreateView

urlpatterns = [
    # Inclui as URLs do app website
    path('', include('web.urls', namespace='web')),

    # Interface administrativa
    path('admin/', admin.site.urls),

    path('usuarios/', UsuarioListView.as_view(), name='lista_usuarios'),

    path('usuario/<id>', UsuarioUpdateView.as_view(), name='atualiza_usuario'),

    path('usuario/excluir/<pk>', UsuarioDeleteView.as_view(), name='delete_usuario'),

    path('usuario/cadastrar/', UsuarioCreateView.as_view(), name='cadastra_usuario'),

]
