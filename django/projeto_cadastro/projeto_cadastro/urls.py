from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsavel, nome de referencia

    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('usuarios/', views.usuarios, name='lista_usuarios'),


] 
