"""User model definition."""

# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Project
from utils.models import BaseModel


class User(BaseModel, AbstractUser):

    username_regex = RegexValidator(regex='[aA0-zZ9]', message='Only letters and numbers allowed')
    username = models.CharField('username', max_length=20, unique=True, validators=[username_regex],
                                help_text='Maximum 20 characters, only letters and numbers',
                                error_messages={'unique': 'Username in use'})
    email = models.EmailField('email address', unique=True, error_messages={'unique': 'Email in use'})
    # AbstractUser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
