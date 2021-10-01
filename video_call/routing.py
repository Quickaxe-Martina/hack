# chat/routing.py
from django.urls import re_path

from video_call.consumers import VideoCallSignalConsumer

websocket_urlpatterns = [
    re_path(r'ws/video_call/(?P<pk>\w+)/$', VideoCallSignalConsumer.as_asgi()),
]
