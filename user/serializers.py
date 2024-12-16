from rest_framework import serializers

from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    this serializer class is used to register a new user
    """
    class Meta:
        model = User
        fields = ('phone_number',)

class UserLoginSerializer(serializers.ModelSerializer):
    """
    this serializer class is used to login a user
    """
    code = serializers.CharField(write_only=True,max_length=5)
    class Meta:
        model = User
        fields = ('phone_number','code')


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    this serializer class is used to update a user
    """
    class Meta:
        model =User
        fields = ('username','first_name','last_name','phone_number','avatar')


class UserListSerializer(serializers.ModelSerializer):
    """
    this serializer class is used to list all users
    """
    class Meta:
        model = User
        fields = ('username','first_name','last_name','phone_number','avatar')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'