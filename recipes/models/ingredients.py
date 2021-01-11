"""Ingredient model definition."""

# Django
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

# Project
from utils.models import BaseModel


class IngredientComposition(models.Model):
    """Representation of the amount of a specific ingredient that a recipe has."""

    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, null=False)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, null=False, related_name='ingredients_list')
    quantity = models.DecimalField(max_digits=21, decimal_places=3, null=False, default=1)

    def save(self, *args, **kwargs):
        if float(self.quantity) <= 0:
            raise ValidationError('Ingredient quantity cannot be equal or less than zero')
        return super(IngredientComposition, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} of {self.ingredient}'


class Ingredient(BaseModel):
    """Representation of an ingredient which can be in different recipes."""

    name_regex = RegexValidator(regex='[aA0-zZ9]', message='Only letters and numbers allowed')
    name = models.CharField(blank=False, max_length=25, unique=True, validators=[name_regex],
                            help_text='Maximum 25 characters, only letters and numbers',
                            error_messages={'unique': 'Ingredient already exists'})

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
