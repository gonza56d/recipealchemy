"""Users api urls."""

# Django
from django.urls import path

# Project
from api.users.views import oauth


urlpatterns = [
    path('users/oauth/', oauth, name='oauth'),
]
