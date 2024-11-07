# urls.py principal do projeto
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),  # Inclui as URLs com o namespace 'website'
]
