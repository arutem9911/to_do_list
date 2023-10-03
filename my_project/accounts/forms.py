import django.contrib.auth.forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-3 mb-3'
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mt-3 mb-3'
            }
        )
    )