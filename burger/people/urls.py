from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^profile",
        views.create_account, name="create_account"),
    url(r"^detail/(?P<username>[^/]*)/$",
        views.profile_detail, name="profile_detail"),
]
