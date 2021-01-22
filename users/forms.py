"""User forms."""

# Django
from django import forms


class LoginForm(forms.Form):

    username_or_email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(required=True)

    def get_cleaned_data(self):
        if self.is_valid():
            username_or_email = self.cleaned_data.get('username_or_email')
            password = self.cleaned_data.get('password')
            return username_or_email, password


class SignupForm(forms.Form):

    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(max_length=56, required=True)

    def get_cleaned_data(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            return username, email, password
