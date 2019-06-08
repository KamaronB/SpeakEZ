# mysite/routing.py
from django.conf.urls import url
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from profiles import consumers



application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter(
        [
        path('ws/room/<uuid:room_name>', consumers.ChatConsumer)
        ]
        )

        )
    ),
})
