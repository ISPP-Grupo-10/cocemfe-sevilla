from django.urls import path
from .views import view_suggestion


urlpatterns = [
    path('view_suggestion/<int:pk>/', view_suggestion, name='view_suggestion'),
]