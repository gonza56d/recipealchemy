"""Api documentation urls."""

# Django
from django.urls import path

# Project
from apidocumentation.views import api_documentation


urlpatterns = [
    path('', api_documentation, name='api_documentation'),
]
