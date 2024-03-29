from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'base' 

urlpatterns = [
    path('', views.pagina_base, name='pagina_base'),
    path('politica_terminos/', views.politica_terminos, name='politica_terminos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
