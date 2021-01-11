"""Ingredient serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from recipes.models import Ingredient, IngredientComposition


class IngredientCompositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientComposition
        fields = ['ingredient', 'recipe', 'quantity']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['name', 'created', 'modified']
