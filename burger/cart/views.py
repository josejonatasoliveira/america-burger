from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models.signals import m2m_changed
from burger.order.models import Order, OrderItem
from django.forms.models import model_to_dict
from channels.layers import get_channel_layer
from burger.burguer.models import Burguer
from .forms import CartAddOrderItemForm
from asgiref.sync import async_to_sync
from burger.offer.models import Offer
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from .models import Cart
import datetime
import json




def checkout_order(cart=None, order_item=None):


  for item in cart.__iter__():

    order, has_create = Order.objects.get_or_create(
      final_value=item['total_price']
    )

    order_i, created = OrderItem.objects.get_or_create(
      order=order,
      burger=order_item,
      quantity=item['quantity'],
      final_price=item['total_price']
    )

@require_POST
def cart_add(request, order_item_id, **kwargs):
    cart = Cart(request)
    order_item = get_object_or_404(Burguer, hash_id=order_item_id)

    form = CartAddOrderItemForm(request.POST)

    data = { 'status': 200 }
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(order_item=order_item,
                        quantity=cd['quantity'],
                        update_quantity=cd['update'])

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event":"cart",
                       "quantity": cd['quantity'],
                       "total_price": str(cart.get_total_price())})
        # checkout_order(cart, order_item)
    
        return JsonResponse(data)

    data['status'] = 400
    return JsonResponse(data)


def cart_remove(request, order_item_id):
    cart = Cart(request)
    order_item = get_object_or_404(Burguer, hash_id=order_item_id)
    cart.remove(order_item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    offers_slide = Offer.objects.filter(Q(category__identifier='slide' ) & Q(available=1 ) & Q(end_date__gte=datetime.datetime.now())).order_by('-start_date')[:3]
    offers_banner = Offer.objects.filter(Q(category__identifier='banner') & Q(available=1)).order_by('-start_date')[:3]
    products = Burguer.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddOrderItemForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    return render(request, 'index.html', 
    context={
      'offers_slide':offers_slide,
      'offers_banner':offers_banner,
      'products':products,
      'cart':cart
    })

m2m_changed.connect(cart_add, sender=Cart)