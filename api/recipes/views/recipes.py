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
