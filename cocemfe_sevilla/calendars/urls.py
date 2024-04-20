from django.contrib import admin
from django.urls import path
from . import views

app_name = 'calendars'

urlpatterns = [
    path('create', views.new_event, name='create_event'),
    path('', views.calendar, name='calendar'),
    path('all_events', views.devolver_eventos, name='all_events'),
]