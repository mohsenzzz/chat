import os
from config import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='avatars/',null=True, blank=True)

    def __str__(self):
        return self.username


    @classmethod
    def get_token_for_user(cls, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @classmethod
    def get_user_info_by_token(cls, token):
        token_string = str(token)
        access_token = AccessToken(token_string)
        user_id = access_token['user_id']
        user = User.objects.filter(id=user_id).first()
        return user

    @classmethod
    def remove_pre_avatar(cls, user):

        image_path = os.path.join(settings.MEDIA_ROOT, str(user.avatar))
        if os.path.exists(image_path):
            os.remove(image_path)