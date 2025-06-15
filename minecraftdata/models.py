from django.db import models

# Create your models here.

# Items Table 1:*
class Item(models.Model):
    name = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)

# Table of recipes => Result of crafting recipes
class Recipes(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
"""
PK  int not null increment
FK Items Table
"""

# Intermediate Table => Store the relations between the recipees and the items used for it.
class RecipeIngredient(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    amount = models.IntegerField()
"""
PK int not null
FK Recipe ID
FK Item ID
int Amount 
"""