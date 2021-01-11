"""Recipe admins declaration."""

# Django
from django.contrib import admin

# Project
from recipes.models import Recipe, Ingredient, IngredientComposition


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('name', 'user', 'created', 'modified')
    list_filter = ('name', 'user', 'ingredients', 'created', 'modified')
    search_fields = ('name', 'user', 'ingredients', 'created', 'modified')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(IngredientComposition)
class IngredientCompositionAdmin(admin.ModelAdmin):

    list_display = ('recipe', 'ingredient', 'quantity')
    list_filter = ('recipe', 'ingredient', 'quantity')
    search_fields = ('recipe', 'ingredient', 'quantity')
