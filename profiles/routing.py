from django.urls import path
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from . import consumers

websocket_urlpatterns = [
    path('ws/room/<uuid:room_name>', consumers.ChatConsumer),
]
