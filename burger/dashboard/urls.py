from django.views.generic import TemplateView
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index_view, name='dashboard'),
]