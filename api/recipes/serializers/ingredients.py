"""Ingredient serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from recipes.models import Ingredient, IngredientComposition


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'created', 'modified']


class IngredientCompositionSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.PrimaryKeyRelatedField(source='ingredient.id', queryset=Ingredient.objects.all())
    name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = IngredientComposition
        fields = ['id', 'name', 'quantity']
