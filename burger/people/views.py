from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .serializers import ProfileSignInSerializer
from django.template.loader import get_template
from django.utils.encoding import force_bytes
from django.shortcuts import render, reverse
from django.core.mail import EmailMessage
from burger.people.models import Profile
from burger.tokens import user_tokenizer
from burger.cart.models import Cart
from django.conf import settings
from .forms import ProfileForm
from django.db.models import Q


def create_account(request, template="account/login.html"):
    cart = Cart(request)
    form = ProfileForm(request.POST)
    form.fields['username'] = form.fields['email']
    
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.username = user.email
        user.password = make_password(user.password)
        user.save()
        token = user_tokenizer.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'https://america-burger.com' + reverse('confirm_email', kwargs={'user_id': user_id, 'token': token})
        message = get_template('account/register_email.html').render({
            'confirm_url': url
        })
        mail = EmailMessage('América Burger - Confirmação de e-mail', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'account/login.html', {
            'message':'Um e-mail de confirmação foi enviado para ' + user.email + '. Por favor confirme para prosseguir com o cadastro.',
            'cart':cart
        })
    return render(request, "index.html", {'cart': cart})


def profile_detail(request, username):
    cart = Cart(request)
    profile = get_object_or_404(Profile, Q(is_active=True), username=username)

    return render(request, "profile_detail.html", {'profile': profile, 'cart': cart})

