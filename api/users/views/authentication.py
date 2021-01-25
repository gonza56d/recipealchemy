"""User authentication views."""

# Django
from django.contrib import auth
from django.db import IntegrityError

# REST Framework
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Project
from api.exceptions.client_errors import DuplicateUserException
from api.users.serializers import UserSerializer
from users.forms import LoginForm, SignupForm
from users.models import User


@api_view(['POST'])
def oauth(request):
    form = LoginForm(data=request.data)
    if form.is_valid():
        username_or_email, password = form.get_cleaned_data()
        user = auth.authenticate(username=username_or_email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_up(request):
    form = SignupForm(data=request.data)
    if form.is_valid():
        username, email, password = form.get_cleaned_data()
        try:
            user = User.objects.create_user(username, email, password)
            if user is not None:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except IntegrityError:
            raise DuplicateUserException
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
