from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from myapp import routing as echo_routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            echo_routing.websocket_urlpatterns
        )
    )
})
