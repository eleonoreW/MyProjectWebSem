from django.contrib import admin
from .models import Recette, Ingredient


class ChoiceInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class RecetteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['recette_description']}),
        ('Description', {'fields': ['recette_instructions','nombre_part','image']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Recette, RecetteAdmin)
