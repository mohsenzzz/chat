from rest_framework import serializers

from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number',)

class UserLoginSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True,max_length=5)
    class Meta:
        model = User
        fields = ('phone_number','code')