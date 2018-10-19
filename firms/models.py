from django.db import models
from django.utils import timezone
from django.db.models import Count

class Recipe(models.Model):
    title = models.CharField(verbose_name='Рецепт', max_length=255)
    description = models.TextField()

    # def rec(self):
    #     return self.id

class IngredientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().values('recipe_id').distinct()

class Instruction(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    # ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    description = models.TextField(verbose_name='Инструкции Описание')

class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Ингредиенты Описание', max_length=255)
    # instruction = models.ForeignKey(Instruction, blank=True, null=True, on_delete=models.CASCADE)
    # objects = models.Manager()
    # ingr_objects = IngredientManager()


    # def show_one_instance(self):
        # fil = Ingredient.objects.all()
        # fil = Ingredient.objects.filter(description='цке')
        # fil2 = fil.description
        # for i in self.description:
        # fil = self.description
        # fil2 = fil.first()
        # return self.description
        # return self.description.all()
        # return self.recipe
        # return fil
        # return self.filter(description__icontains='Это').count()
        # return self.recipe.description
        #  ingredient.description.all()
    # class Meta:
    #     ordering = ('description', )


class IngredientManager(models.Manager):
    def get_queryset(self):
        # distinct = super().get_queryset().values('recipe_id', 'description').order_by('recipe_id').distinct()
        distinct = super().get_queryset().order_by('recipe_id').values_list('recipe_id', flat=True).distinct()
        # distinct = super().get_queryset().values('recipe_id').distinct()
        # reci = super().get_queryset().values('recipe_id').distinct()
        # .values('description', 'recipe_id')
        # .values_list('recipe_id').order_by('description').distinct()
        # .values('recipe_id').distinct().filter(id=8).order_by('description')
        # return reci.all()
        # distinct = super().get_queryset().values('recipe_id').annotate(recipe_id_count=Count('recipe_id')).filter(recipe_id_count=1)
        # records = super().get_queryset().filter(recipe_id__in=[item['recipe_id'] for item in distinct])
        return distinct

class IngredientProxy(Ingredient):
    @property
    def __str__(self):
        return self.objects.all()
    # def get_queryset(self):
    #     return Ingredient.objects.all()
    # objects = models.Manager()
    # ingr_objects = IngredientManager()

    # class Meta:
        # proxy = True
        # ordering = ('description', )

    # def ret(self):
        # self.description = d
        # return d1
        # return super().get_queryset().filter(id=10)
        # values('recipe_id').distinct()



