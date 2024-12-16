from rest_framework import serializers

from user.models import User
from user.serializers import UserListSerializer, UserSerializer
from .models import Chat,Message


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = Chat
        fields = ('token','user')



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['chat','sender','content','created_at']


class ChatUserSerializer(serializers.ModelSerializer):
    # user=UserSerializer(many=True)
    messages=MessageSerializer(many=True)
    class Meta:
        model = Chat
        fields = ('token','user','messages')