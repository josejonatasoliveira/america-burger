from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'burger.cart'

    def ready(self):
        import burger.notifier.signals
