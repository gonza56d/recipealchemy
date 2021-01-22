"""User forms."""

# Django
from django import forms


class LoginForm(forms.Form):

    username_or_email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(required=True)
