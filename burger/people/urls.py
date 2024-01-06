from django.urls import path
from . import views

urlpatterns = [
    path(r"^profile",
        views.create_account, name="create_account"),
    path(r"^detail/(?P<username>[^/]*)/$",
        views.profile_detail, name="profile_detail"),
]
