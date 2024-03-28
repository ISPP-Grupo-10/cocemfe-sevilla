# En el archivo urls.py de tu aplicación 'votings'
from django.urls import path
from .views import *

app_name = "votings"

urlpatterns = [
    path('vote/<int:suggestion_id>/', voting_vote, name='voting_vote'),
]