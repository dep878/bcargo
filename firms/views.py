from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django_tables2 import RequestConfig, SingleTableView

from .forms import IngredientFormSet, InstructionFormSet, RecipeForm
from .models import Recipe, Ingredient, Instruction, IngredientProxy
from .tables import RecipeTable

class RecipeList(SingleTableView):
    model = Recipe
    table_class = RecipeTable
    template_name = 'company_list.html'

    # def get_queryset(self):
    #     return Ingredient.objects.distinct('recipe_id')
    #     # queryset = Ingredient.objects.all()
        # return IngredientProxy.objects.order_by('recipe_id').values_list('recipe_id', flat=True).distinct()
        # return IngredientProxy.ingr_objects.all()
        # .objects.values('description').distinct()
        # objects.all()
        # .values('recipe_id')
        # .filter(id=8)
        # .all()
        # return Ingredient.objects.filter(id=8)
        # r = Recipe.objects.get(id=1)
        # return r.ingredient_set.all()

    # def recipe(request):
    #     table = RecipeTable(Ingredient.objects.all())
    #     RequestConfig(request).configure(table)
    #     return render(request, 'company_list.html', {'table': table})

class CompanyList(ListView):
    template_name = 'company_list.html'
    model = Recipe

class RecipeCreateView(CreateView):
    # template_name = 'company_form.html'
    template_name = 'recipe_add.html'
    model = Recipe
    form_class = RecipeForm
    # success_url = 'company-list'
    success_url = reverse_lazy('company-list')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))

class RecipeUpdateView(UpdateView):
    template_name = 'recipe_add.html'
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        self.success_url = '/account/dashboard/'
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = RecipeForm(self.request.POST, instance=self.object)
            context['ingredient_form'] = IngredientFormSet(self.request.POST, instance=self.object)
            context['instruction_form'] = InstructionFormSet(self.request.POST, instance=self.object)
        else:
            context['form'] = RecipeForm(instance=self.object)
            context['ingredient_form'] = IngredientFormSet(instance=self.object)
            context['instruction_form'] = InstructionFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form, instruction_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  instruction_form=instruction_form))