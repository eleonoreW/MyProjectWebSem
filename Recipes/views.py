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
    return render(request, 'Recipes/detail.html', {'recipe': recipe})

def productdetail(request, product_id):
    product = Produit2.objects.filter(id = product_id)
    context = {'product_id' : product_id, 'product' : product[0]}
    return render(request, 'Recipes/productDetail.html', context)

def myrecipe(request):
        if request.method == "POST":
            form = RecipeForm(request.POST)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('/Recipes/'+str(recipe.id)+'/')
        else:
            form = RecipeForm()
            return render(request, 'Recipes/myRecipe.html', {'form': form})



def search(request):
    research = ""
    context = {}
    if (request.method == 'POST'):
        searchName = request.POST['searchName']

        if searchName != "":
            research = searchName
            results = Produit2.objects.filter(product_name__icontains = searchName)[:100]
            context = {'research': research, 'results':results}

    return render(request, 'Recipes/search.html', context)


