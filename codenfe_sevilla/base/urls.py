from django.contrib import admin
from django.urls import path
from . import views

app_name = 'base' 

urlpatterns = [
    path('', views.pagina_base, name='pagina_base'),
    
]
