from burger.offer.models import Offer, TicketRaffle
from burger.people.models import Profile
from django.contrib import admin
from .forms import OfferForm

class OfferAdmin(admin.ModelAdmin):
  reversion_enable = True

class ProfileInline(admin.TabularInline):
    model = Profile

class TicketAdmin(admin.ModelAdmin):
  reversion_enable = True
  search_fields = ['code']

admin.site.register(TicketRaffle,TicketAdmin)
admin.site.register(Offer,OfferAdmin)