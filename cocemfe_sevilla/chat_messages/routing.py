import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("" , ChatConsumer.as_asgi()) , 
] 