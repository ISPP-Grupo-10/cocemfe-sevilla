from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.map_index, name='map_index'),
    path('<str:latitude>/<str:longitude>', views.map_search, name='map_search'),
]