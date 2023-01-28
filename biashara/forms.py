from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Business,Business_sector,Amount


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]