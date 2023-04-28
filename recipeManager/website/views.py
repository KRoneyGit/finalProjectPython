from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure
import pandas as pd


# Create your views here.
def home(request):
    recipe_list = Recipe.objects.all
    return render(request, 'home.html', {'recipe_list': recipe_list})


def charts(request):
    recipe_list = Recipe.objects.all()
    my_frame = pd.DataFrame([vars(s) for s in recipe_list])
    my_frame.drop('_state',axis='columns',inplace=True)

    entree = my_frame['category'].value_counts()['Entree']
    side = my_frame['category'].value_counts()['Side']
    dessert = my_frame['category'].value_counts()['Dessert']
    snack = my_frame['category'].value_counts()['Snack']

    easy = my_frame['difficulty'].value_counts()['Easy']
    medium = my_frame['difficulty'].value_counts()['Medium']
    hard = my_frame['difficulty'].value_counts()['Hard']

    difficulties = ['Easy', 'Medium', 'Hard']
    difficulty = [easy, medium, hard]
    categories = ['Entree', 'Side', 'Dessert', 'Snack']
    category = [entree, side, dessert, snack]

    plot1 = figure(x_range=categories, height=350, title="Category counts", toolbar_location=None, tools="")
    plot1.vbar(x=categories, top=category, width=0.5)
    plot1.xgrid.grid_line_color = None
    plot1.y_range.start = 0

    script1, div1 = components(plot1, CDN)

    plot2 = figure(x_range=difficulties, height=350, title="Difficulty counts", toolbar_location=None, tools="")
    plot2.vbar(x=difficulties, top=difficulty, width=0.5)
    plot2.xgrid.grid_line_color = None
    plot2.y_range.start = 0

    script2, div2 = components(plot2, CDN)

    return render(request, 'charts.html',{'recipe_list': recipe_list, 'the_script1': script1, 'the_div1': div1, 'the_script2': script2, 'the_div2': div2})


def add_recipe(request):
    if (request.method == "POST"):
        form = RecipeForm(request.POST or None)
        if (form.is_valid()):
            form.save()
            recipe_list = Recipe.objects.all
            return render(request, 'home.html', {'recipe_list': recipe_list})
        else:
            return render(request, 'add_recipe.html', {})
    else:
        return render(request, 'add_recipe.html', {})


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    recipe_list = Recipe.objects.all
    return render(request, 'home.html', {'recipe_list': recipe_list})


def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if (form.is_valid()):
        form.save()
        recipe_list = Recipe.objects.all
        return render(request, 'home.html', {'recipe_list': recipe_list})
    return render(request, 'update_recipe.html', {'recipe': recipe, 'recipe_id': recipe_id})