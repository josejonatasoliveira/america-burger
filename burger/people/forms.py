import taggit

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = (
            'user',
            'profile',
            'last_login',
            'groups',
            'user_permissions',
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined',
            'cpf',
            'address',
            'hash_id',
            'tickets',
            'company')
