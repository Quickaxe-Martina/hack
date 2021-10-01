from django.urls import re_path

from accounts.consumers import UserConsumer

websocket_urlpatterns = [
    re_path(r'ws/user/(?P<pk>\w+)/$', UserConsumer.as_asgi()),  # TODO:
]
