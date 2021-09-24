from .models import TopicCategory, TopicType
from .forms import TopicCategoryForm
from django.contrib import admin
# Register your models here.

class TopicCategoryAdmin(admin.ModelAdmin):
    form = TopicCategoryForm

class TypeInline(admin.TabularInline):
    model = TopicCategoryForm

class TopicTypeAdmin(admin.ModelAdmin):
    reversion_enable = True
    inlines = [TypeInline]
    list_display_links = ('identifier',)
    list_display = (
        'identifier',
        'description',
        'fa_class')
    search_fields=('description',)

admin.site.register(TopicCategory, TopicCategoryAdmin)
admin.site.register(TopicType)
