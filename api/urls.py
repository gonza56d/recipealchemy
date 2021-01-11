"""Api urls."""

# Django
from django.urls import include, path


urlpatterns = [
    path('', include('api.recipes.urls')),
]
