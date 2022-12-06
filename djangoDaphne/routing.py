from django.urls import path
from djangoDaphne.consumers import EchoConsumer
from djangoDaphne.websockets_django import MyConsumer
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
    path('echo/', MyConsumer.as_asgi()),
    path('', MyConsumer.as_asgi())
]