"""Recipe views implementation."""

# REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Project
from api.exceptions.client_errors import MissingFieldException
from api.recipes.serializers import RecipeSerializer, RecipeStepSerializer, IngredientCompositionSerializer
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            IngredientCompositionSerializer(data=request.data['ingredients_list'])
        except KeyError:
            raise MissingFieldException(field='ingredients_list')
        try:
            RecipeStepSerializer(data=request.data['steps'])
        except KeyError:
            raise MissingFieldException(field='setps')
        self.serializer_class(data=request.data)
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        username = self.request.query_params.get('user', None)
        recipe = self.request.query_params.get('recipe', None)
        description = self.request.query_params.get('description', None)
        ingredients = self.request.query_params.get('ingredients', None)
        if username:
            self.queryset = self.queryset.filter(user__username=username.lower().strip())
        if recipe:
            self.queryset = self.queryset.filter(name__icontains=recipe.strip())
        if description:
            self.queryset = self.queryset.filter(description__icontains=description.strip())
        if ingredients:
            ingredients = RecipeViewSet.remove_not_numbers(ingredients)
            self.queryset = self.queryset.filter(ingredients__in=ingredients)
        return self.queryset

    @staticmethod
    def remove_not_numbers(csv):
        """Remove not numeric values from comma separated values string and return a list of integers."""
        ing = [i.strip() for i in csv.split(',')]
        csv = []
        for i in ing:
            try:
                csv.append(int(i))
            except ValueError:
                pass
        return csv
