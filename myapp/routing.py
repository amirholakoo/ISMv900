# from django.urls import path
# from .consumers import AlertConsumer
#
# websocket_urlpatterns = [
#     path('ws/', AlertConsumer)
# ]

# websocket_urlpatterns = [
#     re_path(r'ws/alert/$', consumers.AlertConsumer.as_asgi()),
# ]
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/alert/$', consumers.AlertConsumer.as_asgi()),
# ]
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/alert/', consumers.AlertConsumer.as_asgi()),
]
