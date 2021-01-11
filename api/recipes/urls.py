"""Recipes api urls."""

# Django
from django.urls import path, include

# REST Framework
from rest_framework import routers

# Project
from api.recipes.views import RecipeViewSet

router = routers.SimpleRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
]
