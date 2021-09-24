from .models import Burguer, Ingredient, Review, Photo
from django.contrib import admin

class BurguerAdmin(admin.ModelAdmin):
  reversion_enable = True

class IngredientAdmin(admin.ModelAdmin):
  reversion_enable = True

class ReviewAdmin(admin.ModelAdmin):
  reversion_enable = True

class PhotoAdmin(admin.ModelAdmin):
  reversion_enable = True

admin.site.register(Burguer,BurguerAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Photo,PhotoAdmin)