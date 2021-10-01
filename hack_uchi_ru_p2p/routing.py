from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from accounts.routing import websocket_urlpatterns as ws_user_url
from video_call.routing import websocket_urlpatterns as ws_video_url

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws_user_url + ws_video_url
        )
    ),
})
