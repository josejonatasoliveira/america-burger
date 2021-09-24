from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render_to_response
from django.template import RequestContext
from burger.people.models import Profile
from burger.burguer.models import Burguer
from burger.base.forms import ContactForm
from burger.offer.models import Offer
from django.http import JsonResponse
from burger.cart.models import Cart
from django.shortcuts import render
from .tokens import user_tokenizer
from burger.forms import BaseForm
from django.conf import settings
from django.db.models import Q
from django.views import View
import datetime


# @permission_required("view.add_user")
def index_view(request, template="index.html"):
  cart = Cart(request)

  offers_slide = Offer.objects.filter(Q(category__identifier='slide' ) & Q(available=1 ) & Q(end_date__gte=datetime.datetime.now())).order_by('-start_date')[:3]
  offers_banner = Offer.objects.filter(Q(category__identifier='banner') & Q(available=1)).order_by('-start_date')[:3]
  products = Burguer.objects.all()
  return render(
    request, 
    template,
    context={
      'offers_slide':offers_slide,
      'offers_banner':offers_banner,
      'products':products,
      'cart':cart
    })


def load_menu(request, template="menu.html"):
  return render(request, template)

def save_contact(request, template="about.html"):

  if(request.POST):
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
    return JsonResponse({"message":""})

  return JsonResponse({"message":"Erro ao enviar sua mensagem!"})


class ConfirmRegistrationView(View):
  def get(self, request, user_id, token):
    user_id = force_text(urlsafe_base64_decode(user_id))
    
    user = Profile.objects.get(pk=user_id)

    if user and user_tokenizer.check_token(user, token):
      user.is_active = True
      user.save()

    return render(request, 'account/login.html',{
      'message':'Cadastro realizado com sucesso! Seja bem vindo! :)'
    })


def login(request, template="account/login.html"):
  return render(request, template)

def register(request, template="account/signup.html"):
  return render(request, template)

def reset_password(request, template="account/password_reset.html"):
  return render(request, template)

def about(request, template="about.html"):
  return render(request, template)

def privacy_policy(request, template="privacy_policy.html"):
  return render(request, template)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response(template_name)
    response.status_code = 500
    return response