from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='avatars/',null=True, blank=True)

    def __str__(self):
        return self.username