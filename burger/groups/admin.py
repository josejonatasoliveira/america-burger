from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        GroupMemberInline
    ]
    exclude = ['group', ]


admin.site.register(models.GroupProfile, GroupAdmin)
