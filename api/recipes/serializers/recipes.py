"""Recipe serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from api.recipes.serializers import IngredientCompositionSerializer
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientCompositionSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['user', 'name', 'ingredients', 'created', 'modified']
