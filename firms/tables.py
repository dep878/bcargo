import django_tables2 as tables
from .models import Recipe, Ingredient, Instruction, IngredientProxy
from django_tables2.utils import Accessor

# class InstructionTable(tables.Table):
#     instruction_number = tables.Column(verbose_name='Порядковый номер', orderable=False, accessor='number')
#     instruction_description = tables.Column(verbose_name='Описние инструкции', orderable=False, accessor='instruction.description')

#     class Meta:
#         model = Instruction
#         fields = ('instruction_number', 'instruction_description')

class RecipeTable(tables.Table):
    select = tables.CheckBoxColumn(empty_values=(), footer="")
    title = tables.Column(verbose_name='Рецепт')
    description = tables.Column(verbose_name='Описание рецепта', orderable=False)
    # description = tables.RelatedLinkColumn(verbose_name='Описание рецепта', orderable=False, accessor='recipe.description')
    # ingredient_description = tables.Column(verbose_name='Описние ингредиентов', orderable=True, accessor='description')
    # ingredient_description = tables.RelatedLinkColumn(accessor='description')
    # instruction_number = tables.Column(verbose_name='Порядковый номер', orderable=False, accessor='instruction.number')
    # instruction_description = tables.Column(verbose_name='Описние инструкции', orderable=False, accessor='description')
    # recipe_id = tables.Column(verbose_name='ID', orderable=True, accessor='recipe_id')

    class Meta:
        model = Recipe
        fields = ('select', 'title', 'description')
        sequence = ('select', 'title', 'description')