from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r"^profile",
        views.create_account, name="create_account"),
    re_path(r"^detail/(?P<username>[^/]*)/$",
        views.profile_detail, name="profile_detail"),
]
