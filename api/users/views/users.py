"""User views."""

# REST Framework
from rest_framework import viewsets

# Project
from api.exceptions.client_errors import MethodNotAllowedException
from api.users.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowedException
