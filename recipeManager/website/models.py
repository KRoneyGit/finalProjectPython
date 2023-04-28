from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    servings = models.IntegerField(default=1)
    prep_time = models.IntegerField(default=10)
    cook_time = models.IntegerField(default=0)
    ingredient_list = models.CharField(max_length=500)
    instructions = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=10)

    def __str__(self):
        return self.recipe_name
