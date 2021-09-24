from django.apps import AppConfig


class NotifierConfig(AppConfig):
    name = 'burger.notifier'

    def ready(self):
        from . import signals
