from django.db.models.signals import post_save, pre_save
from channels.layers import get_channel_layer
from burger.people.models import Profile
from burger.people.models import Profile
from asgiref.sync import async_to_sync
from django.dispatch import receiver
from burger.cart.models import Cart


@receiver(pre_save, sender=Cart)
def announce_new_product(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event": "New Product",
                       "username": "Ok"})