from django.shortcuts import render
from burger.cart.models import Cart
from .models import Burguer, Photo
from django.db.models import Q

# Create your views here.

def index_view(request, template="burguer_list.html"):
    return render(request, template)

def burguer_detail(request, id, template="burguer_detail.html"):
    cart = Cart(request)

    product = Burguer.objects.get(hash_id__exact=id)
    photo_list = Photo.objects.filter(Q(burguer_id__exact=product.id))
    
    out = {
        'product': product,
        'photo_list': photo_list,
        'cart':cart
    }

    return render(request, template, out)
