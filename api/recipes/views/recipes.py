"""Recipe viewsets declaration."""

# REST framework
from rest_framework import viewsets
from rest_framework.response import Response

# Project
from api.recipes.serializers import RecipeSerializer
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        username = self.request.query_params.get('user', None)
        recipe = self.request.query_params.get('recipe', None)
        if username is not None:
            self.queryset = self.queryset.filter(user__username=username.lower())
        if recipe is not None:
            self.queryset = self.queryset.filter(name=recipe.lower())
        return self.queryset
