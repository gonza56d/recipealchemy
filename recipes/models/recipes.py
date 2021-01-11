"""Recipe model definition."""

# Django
from django.core.validators import RegexValidator
from django.db import models

# Project
from utils.models import BaseModel


class Recipe(BaseModel):
    """Representation of a recipe which contains different ingredients and proportions of them."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
    name_regex = RegexValidator(regex='[aA0-zZ9]', message='Only letters and numbers allowed')
    name = models.CharField(blank=False, max_length=50, validators=[name_regex],
                            help_text='Maximum 50 characters, only letters and numbers')
    ingredients = models.ManyToManyField('recipes.Ingredient', through='recipes.IngredientComposition')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Recipe, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['user', 'name']
