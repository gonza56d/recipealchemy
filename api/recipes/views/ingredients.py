"""Ingredient views declaration."""

# REST framework
from rest_framework import viewsets

# Project
from api.recipes.serializers import IngredientSerializer
from recipes.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        ingredient = self.request.query_params.get('ingredient', None)
        if ingredient is not None:
            self.queryset = self.queryset.filter(name__icontains=ingredient)
        return self.queryset
