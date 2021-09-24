from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    url(r'^$',
        views.index_view,
        name='burger_list'),
    url(r'^(?P<id>[^/]*)$',views.burguer_detail, name="burguer_detail")
]