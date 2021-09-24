from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<order_item_id>[\w-]+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<order_item_id>[\w-]+)/$', views.cart_remove, name='cart_remove'),
]
