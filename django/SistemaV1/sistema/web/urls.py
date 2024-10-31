from django.urls import path
from . import views


app_name = 'web'

urlpatterns = [
    #GET /
    path('', views.index, name='index'),

]