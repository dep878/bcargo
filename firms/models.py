from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

class Instruction(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()