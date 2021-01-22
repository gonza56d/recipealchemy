"""User authentication views."""

# Django
from django.contrib import auth

# REST Framework
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Project
from users.forms import LoginForm


@api_view(['POST'])
def oauth(request):
    form = LoginForm(data=request.data)
    if form.is_valid():
        username_or_email = form.cleaned_data.get('username_or_email')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username_or_email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Username/email and password must be provided.'}, status=status.HTTP_400_BAD_REQUEST)
