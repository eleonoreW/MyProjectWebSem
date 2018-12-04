from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from Recipes.forms import RecipeForm
from .models import Recette, Ingredient, Product, Produit2


def index(request):
    latest_recipe_list = Recette.objects.order_by('-pub_date')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'Recipes/cookbook.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recette, pk=recipe_id)

    energy = 0
    carbohydrates = 0
    sugars = 0
    fat = 0
    proteins = 0
    fiber =0
    sodium = 0

    for ingredient in recipe.ingredient_set.all():
        energy += (ingredient.id_ingredient.energy_100g * ingredient.quantity // (100 * recipe.nombre_part))
        carbohydrates += (ingredient.id_ingredient.carbohydrates_100g * ingredient.quantity // (100 * recipe.nombre_part))
        sugars += (ingredient.id_ingredient.sugars_100g * ingredient.quantity // (100 * recipe.nombre_part))
        fat += (ingredient.id_ingredient.fat_100g * ingredient.quantity // (100 * recipe.nombre_part))
        proteins += (ingredient.id_ingredient.proteins_100g * ingredient.quantity // (100 * recipe.nombre_part))
        fiber += (ingredient.id_ingredient.fiber_100g * ingredient.quantity // (100 * recipe.nombre_part))
        sodium += (ingredient.id_ingredient.sodium_100g * ingredient.quantity // (100 * recipe.nombre_part))

    context = {'energy': energy,
               'carbohydrates': carbohydrates,
               'sugars': sugars,
               'fat': fat,
               'proteins': proteins,
               'fiber': fiber,
               'sodium': sodium}

    context['pEnergy'] = energy * 100 // 2000
    context['pCarbohydrates'] = carbohydrates * 100 // 270
    context['pSugars'] = sugars * 100 // 90
    context['pFat'] = fat * 100 // 70
    context['pProteins'] = proteins * 100 // 50
    context['pFiber'] = fiber * 100 // 25
    context['pSodium'] = sodium * 100 // 6
    context['recipe'] = recipe

    return render(request, 'Recipes/detail.html', context)


def productdetail(request, product_id):
    product = Produit2.objects.filter(id=product_id)
    pEnergy = product[0].energy_100g * 100 // 2000
    pCarbohydrates = product[0].carbohydrates_100g * 100 // 270
    pSugars = product[0].sugars_100g * 100 // 90
    pFat = product[0].fat_100g * 100 // 70
    pProteins = product[0].proteins_100g * 100 // 50
    pFiber = product[0].fiber_100g * 100 // 25
    pSodium = product[0].sodium_100g * 100 // 6
    context = {'product_id': product_id,'product': product[0]}
    context['pEnergy'] = pEnergy
    context['pCarbohydrates'] = pCarbohydrates
    context['pSugars'] = pSugars
    context['pFat'] = pFat
    context['pProteins'] = pProteins
    context['pFiber'] = pFiber
    context['pSodium'] = pSodium

    return render(request, 'Recipes/productDetail.html', context)


def myrecipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('/Recipes/' + str(recipe.id) + '/')
    else:
        form = RecipeForm()
        return render(request, 'Recipes/myRecipe.html', {'form': form})


def search(request):
    research = ""
    context = {}
    if request.method == 'POST':
        searchName = request.POST['searchName']

        if searchName != "":
            research = searchName
            results = Produit2.objects.filter(product_name__icontains=searchName)[:100]
            context = {'research': research, 'results': results}

    return render(request, 'Recipes/search.html', context)
