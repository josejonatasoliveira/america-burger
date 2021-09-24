from burger.burguer.serializers import BurguerSerializer
from django.forms.models import model_to_dict
from burger.burguer.models import Burguer
from django.shortcuts import render
from django.conf import settings
from decimal import Decimal
from django.db import models

# Create your views here.

class Cart(object):

  def __init__(self, request):
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
        # save an empty cart in the session
        cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart

  def add(self, order_item, quantity=1, update_quantity=False):
    order_item_id = order_item.hash_id
    order = model_to_dict(order_item)

    order['energetic_value'] = str(order['energetic_value'])
    order['weight'] = str(order['weight'])
    order['price'] = str(order['price'])
    order['image_file'] = str(order['image_file'])
    order['quantity'] = quantity

    if order_item_id not in self.cart:
      self.cart[order_item_id] = {
                            'order': order,
                            'quantity': 0,
                            'price':str(order_item.price)}
    if update_quantity:
      self.cart[order_item_id]['quantity'] = quantity
    else:
      self.cart[order_item_id]['quantity'] += quantity
      order['quantity'] += quantity

    self.save()
    return self.cart

  def save(self):
    self.session[settings.CART_SESSION_ID] = self.cart
    self.session.modified = True

  def remove(self, order_item):
    order_item_id = order_item.hash_id
    if order_item_id in self.cart:
      del self.cart[order_item_id]
      self.save()
  
  def __iter__(self):
    order_item_ids = self.cart.keys()
    orders = Burguer.objects.filter(hash_id__in=order_item_ids)
    for order in orders:
      self.cart[str(order.hash_id)]['order'] = order
    
    for item in self.cart.values():
      item['price'] = Decimal(item['price'])
      item['total_price'] = item['price'] * item['quantity']
      yield item

  def __len__(self):
    return sum(item['quantity'] for item in self.cart.values())

  def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

  def clear(self):
      # remove cart from session
      del self.session[settings.CART_SESSION_ID]
      self.session.modified = True