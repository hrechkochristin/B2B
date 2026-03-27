from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255) 
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_carrier = models.BooleanField(default=False)

    def __str__(self):
        return self.username