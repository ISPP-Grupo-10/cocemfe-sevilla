# En el archivo urls.py de tu aplicación 'votings'
from django.urls import path
from .views import voting_statistics, voting_vote

app_name = "votings"

urlpatterns = [
    path('vote/<int:suggestion_id>/', voting_vote, name='voting_vote'),
    path('statistics/<int:pk>/', voting_statistics, name='voting_statistics'),

]