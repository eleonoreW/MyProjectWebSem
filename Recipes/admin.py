from django.contrib import admin
from .models import Recette, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class RecetteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['recette_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Recette, RecetteAdmin)
