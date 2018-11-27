from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from Recipes.models import Recette


def home(request):
    latest_recipe_list = Recette.objects.order_by('-pub_date')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def diets(request):
    return render(request, 'Diets/diets.html')

def regime1(request):
    return render(request, 'Diets/regime1.html')
def regime2(request):
    return render(request, 'Diets/regime2.html')
def regime3(request):
    return render(request, 'Diets/regime3.html')
def regime4(request):
    return render(request, 'Diets/regime4.html')
def regime5(request):
    return render(request, 'Diets/regime5.html')
def regime6(request):
    return render(request, 'Diets/regime6.html')
def regime7(request):
    return render(request, 'Diets/regime7.html')
def regime8(request):
    return render(request, 'Diets/regime8.html')
def regime9(request):
    return render(request, 'Diets/regime9.html')


def detail(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)
    return render(request, 'Recipes/detail.html', {'recipe': recipe})


def myrecipe(request):
    return render(request, 'Recipes/myRecipe.html')


def cookbook(request):
    latest_recipe_list = Recette.objects.order_by('-pub_date')
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'Recipes/cookbook.html', context)
def search(request):
    query = request.GET.get('query')
    if not query:
        Recipes = Recipes.objects.all()
    else:
        Recipes = Recipes.objects.filter(recipe__icontains=query)
    if not Recipes.exists():
        Recipes = Recipes.objects.filter(ingredient__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'recettes': Recipes,
        'ingredients': ingredient
    }
    return render(request, 'store/search.html', context)