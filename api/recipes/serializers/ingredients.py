"""Ingredient serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from recipes.models import Ingredient, IngredientComposition


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['name', 'created', 'modified']


class IngredientCompositionSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = IngredientComposition
        fields = ['name', 'quantity']
