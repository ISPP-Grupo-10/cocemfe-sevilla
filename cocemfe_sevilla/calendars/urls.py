from django.contrib import admin
from django.urls import path
from . import views

app_name = 'calendars'

urlpatterns = [
    path('create', views.new_event, name='create_event'),
    path('all_events', views.all_events, name='all_events'),
]