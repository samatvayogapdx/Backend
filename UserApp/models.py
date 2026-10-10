from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    email=models.EmailField(unique=True)