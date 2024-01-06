from django.views.generic import TemplateView
from django.urls import path
from . import views



urlpatterns = [
    path(r'^$', views.index_view, name='dashboard'),
]