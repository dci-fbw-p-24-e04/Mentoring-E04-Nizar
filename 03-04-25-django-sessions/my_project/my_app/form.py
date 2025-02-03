from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
SEX_CHOICES = [
        ("M","Male"),
        ("F","Female"),
        ("O","Other")
    ]
class UserResgtrationForm(UserCreationForm):
    sex = forms.ChoiceField(choices=SEX_CHOICES,widget=forms.RadioSelect())
    class Meta:
        model = CustomUser
        fields = ("username","email","first_name","last_name","password1","password2","bio","phone_number","age","sex")