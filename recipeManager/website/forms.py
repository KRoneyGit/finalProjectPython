from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'servings', 'prep_time', 'cook_time', 'ingredient_list', 'instructions', 'category', 'difficulty']