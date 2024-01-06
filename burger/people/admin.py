from burger.people.models import Profile
from django.contrib import admin

class PeopleAdmin(admin.ModelAdmin):
  reversion_enable = True
  search_fields=('name',)

admin.site.register(Profile,PeopleAdmin)