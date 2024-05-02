from django.urls import path

from .views import chatPage
from suggestions.views import *

urlpatterns = [
    path("<int:pk>/", chatPage, name="chat_view"),
]
