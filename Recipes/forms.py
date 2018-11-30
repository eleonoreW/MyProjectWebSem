from django.forms import ModelForm

from Recipes.models import Recette


class RecipeForm(ModelForm):
     class Meta:
         model = Recette
         fields = [ 'recette_description', 'recette_instructions', 'nombre_part','image']