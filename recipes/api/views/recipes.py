"""Recipe viewsets declaration."""

# REST framework
from rest_framework import viewsets

# Project
from recipes.api.serializers import RecipeSerializer
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
