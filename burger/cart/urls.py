from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.cart_detail, name='cart_detail'),
    path(r'^add/(?P<order_item_id>[\w-]+)/$', views.cart_add, name='cart_add'),
    path(r'^remove/(?P<order_item_id>[\w-]+)/$', views.cart_remove, name='cart_remove'),
]
