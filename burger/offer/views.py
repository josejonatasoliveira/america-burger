from .models import Offer, TicketRaffle
from burger.people.models import Profile
from django.http import JsonResponse
from django.http import HttpResponse
from burger.cart.models import Cart
from django.shortcuts import render
from django.db.models import Q
import datetime

def index_view(request, template="raffle.html"):
    cart = Cart(request)

    if(request.method != "POST"):
        raffle = Offer.objects.filter(Q(category__identifier='sorteio' ) & Q(available=1 )).order_by('-start_date')[:1]
        offers_banner = Offer.objects.filter(Q(category__identifier='sorteio-banner') & Q(available=1)).order_by('-start_date')[:2]
        
        return render(request, template, context={ "raffle":raffle[0], "offers_banner": offers_banner })

    else:
        try:
            ticket = TicketRaffle.objects.get(Q(code__iexact=request.POST['code'].upper()) & Q(active=0))
            ticket.active = True
            ticket.save()

            request.user.tickets.add(ticket)
            request.user.save()

            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(status=404)