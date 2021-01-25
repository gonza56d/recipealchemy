"""User serializers declaration."""

# REST Framework
from rest_framework import serializers

# Project
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['username', 'email', 'created', 'modified']
