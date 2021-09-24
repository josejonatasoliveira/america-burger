from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from burger.notifier.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", NoseyConsumer),
    ])
})