"""Base model definition."""

# Django
from django.db import models


class BaseModel(models.Model):
    """Base model with utility attributes such as creation and modification dates."""

    created = models.DateTimeField('created at', auto_now_add=True, help_text='Date of creation')
    modified = models.DateTimeField('last modified', auto_now=True, help_text='Date of last modification')

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
