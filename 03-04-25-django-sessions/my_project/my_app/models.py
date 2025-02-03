from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ("M","Male"),
        ("F","Female"),
        ("O","Other")
    ]
    phone_number = models.CharField(max_length=40,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    sex = models.CharField(choices=SEX_CHOICES,max_length=10)
    age = models.PositiveIntegerField(blank=True,null=True)




