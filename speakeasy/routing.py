from django.urls import path
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from profiles.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter(
         [
         path('profile/chat/room/<uuid:room_name>/', ChatConsumer),
         ]
        )

        )
    ),
})
