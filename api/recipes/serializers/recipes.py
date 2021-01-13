"""Recipe serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from api.recipes.serializers import IngredientCompositionSerializer
from api.users.serializers import UserSerializer
from recipes.models import Recipe, RecipeStep


class RecipeStepSerializer(serializers.ModelSerializer):

    recipe_id = serializers.PrimaryKeyRelatedField(source='recipe.id', queryset=Recipe.objects.all())
    recipe_name = serializers.ReadOnlyField(source='recipe.name')

    class Meta:
        model = RecipeStep
        fields = ['recipe_id', 'recipe_name', 'step_number', 'title', 'description']


class RecipeSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True, many=False)
    id = serializers.ReadOnlyField()
    ingredients_list = IngredientCompositionSerializer(read_only=True, many=True)
    steps = RecipeStepSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['user', 'id', 'name', 'description', 'ingredients_list', 'steps', 'created', 'modified']
