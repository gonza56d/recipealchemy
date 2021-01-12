"""Recipe views declaration."""

# REST framework
from rest_framework import viewsets

# Project
from api.recipes.serializers import RecipeSerializer
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

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
