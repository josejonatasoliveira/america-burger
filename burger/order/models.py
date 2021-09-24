from django.utils.translation import ugettext_lazy as _
from burger.burguer.models import Burguer
from django.conf import settings
from datetime import datetime
from django.db import models
import uuid

class Order(models.Model):
    timestamp = models.DateTimeField(default=datetime.now())
    value = models.DecimalField(
        _('Valor'),
        help_text="Preço de cada ticket",
        decimal_places=2,
        default=0.00,
        max_digits=20
    )
    discount = models.DecimalField(
        _('Desconto Final'),
        help_text="Desconto sobre o ticket se houver",
        decimal_places=2,
        default=0.00,
        max_digits=20
    )
    final_value = models.DecimalField(
        _("Valor Final"),
        help_text="Valor final da compra",
        decimal_places=2,
        default=0.00,
        max_digits=20
    )
    is_paid = models.BooleanField(
        _('Foi pago'),
        help_text="Se a compra foi paga",
        default=True
    )

    class Meta:
        db_table = 'ord_order'
        verbose_name = 'Ordem'
        verbose_name_plural = "Ordens"


class OrderItem(models.Model):
    hash_id = models.TextField(
        default=str(uuid.uuid4()), unique=True
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    burger = models.ForeignKey(Burguer, on_delete=models.PROTECT, null=True)
    quantity = models.IntegerField(
        _("Quantidade do Item"),
        default=1
    )
    final_price = models.DecimalField(
        _("Preço Final"),
        default=0.0,
        decimal_places=2, 
        max_digits=20
    )

    class Meta:
        verbose_name = "Item da Ordem"
        verbose_name_plural = "Itens da Ordem"
        db_table = "order_item"

    @property
    def total(self):
        return self.quantity * self.order.final_value
    
    @property
    def augment_quantity(self, quantity):
        self.quantity += int(quantity)
        self.save()
    
    def save(self, *args, **kwargs):
        list_hash_id = OrderItem.objects.values_list('hash_id', flat=True)
        
        if self.hash_id in list_hash_id:
            self.hash_id = str(uuid.uuid4())

        super(OrderItem, self).save()

