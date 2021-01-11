"""User model definition."""

# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Project
from utils.models import BaseModel


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, birthday, **extra_fields):
        """
        Create and save a user with the given username, email, password, and birthday.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.birthday = birthday
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, birthday=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, birthday, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(BaseModel, AbstractUser):

    username_regex = RegexValidator(regex='[aA0-zZ9]', message='Only letters and numbers allowed')
    username = models.CharField('username', max_length=20, unique=True, validators=[username_regex],
                                help_text='Maximum 20 characters, only letters and numbers',
                                error_messages={'unique': 'Username in use'})
    email = models.EmailField('email address', unique=True, error_messages={'unique': 'Email in use'})
    birthday = models.DateField(null=True)
    # AbstractUser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
