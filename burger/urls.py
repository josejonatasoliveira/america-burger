"""burger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views
from .tokens import user_tokenizer
from . import views as index_view
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^jet/', include('jet.urls')),
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r"^account/", include("allauth.urls")),
    url(r'^$',index_view.index_view,name='home'),
    url(r'^cart/', include(('burger.cart.urls', 'cart'), namespace='cart')),
    url(r'^login/', index_view.login,name='login'),
    url(r'^about/', index_view.about,name='about'),
    url(r'^privacy_policy/', index_view.privacy_policy,name='privacy_policy'),
    url(r'^contact', index_view.save_contact, name="save_contact"),
    url(r'^reset/', index_view.reset_password,name='reset'),
    url(r'^register/', index_view.register,name='register'),
    url(r'^profile/', include('burger.people.urls')),
    url(r'^burger/', include('burger.burguer.urls')),
    url(r'^dashboard/', include('burger.dashboard.urls')),
    url(r'^raffle/', include('burger.offer.urls')),
    url(r'^menu/', index_view.load_menu, name="menu"),
    url(
    r'^reset-password/',
    PasswordResetView.as_view(
      template_name='account/password_reset.html',
      html_email_template_name='account/reset_password_email.html',
      success_url=settings.LOGIN_URL,
      token_generator=user_tokenizer),
      name='reset_password'
    ),
    url(
    'reset-password-confirmation/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    PasswordResetConfirmView.as_view(
      template_name='account/reset_password_update.html', 
      post_reset_login=True,
      post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
      token_generator=user_tokenizer,
      success_url=settings.LOGIN_REDIRECT_URL),
      name='password_reset_confirm'
    ),
    url('confirm-email/(?P<user_id>[0-9A-Za-z]+)-(?P<token>.+)/$', index_view.ConfirmRegistrationView.as_view(), name='confirm_email'),
] + i18n_patterns(
    url(r'^admin/', admin.site.urls)
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.LOCAL_MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
handler404 = 'burger.views.handler404'                      
admin.site.site_header = 'América Burger'                    
