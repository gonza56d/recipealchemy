"""Authentication backends."""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

# Project
UserModel = get_user_model()


class UserBackend(ModelBackend):
    """Authentication logic.

    Implement authentication with either username or email, and password."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        username = username.lower()
        try:
            user = UserModel._default_manager.get(Q(username=username) | Q(email=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
