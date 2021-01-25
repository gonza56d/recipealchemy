"""Users api urls."""

# Django
from django.urls import path

# Project
from api.users.views import oauth, sign_up


urlpatterns = [
    path('users/oauth/', oauth, name='oauth'),
    path('users/signup/', sign_up, name='signup'),
]
