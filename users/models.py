from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('superadmin', 'Super Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)