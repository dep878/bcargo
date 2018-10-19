from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Recipe, Ingredient, Instruction

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        # exclude = ['created_date']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class InstructionForm(ModelForm):
    class Meta:
        model = Instruction
        fields = '__all__'

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form=InstructionForm, extra=1)
