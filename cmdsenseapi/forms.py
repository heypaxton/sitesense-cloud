from django import forms
from .models import *
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=32)
    username = forms.EmailField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    tac = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password', 'tac']
