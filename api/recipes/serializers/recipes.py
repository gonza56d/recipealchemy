"""Recipe serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from api.recipes.serializers import IngredientCompositionSerializer
from api.users.serializers import UserSerializer
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True, many=False)
    ingredients_list = IngredientCompositionSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['user', 'id', 'name', 'ingredients_list', 'created', 'modified']
