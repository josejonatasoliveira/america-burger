from burger.people.models import Profile
from django.contrib import admin

class PeopleAdmin(admin.ModelAdmin):
  reversion_enable = True

admin.site.register(Profile,PeopleAdmin)