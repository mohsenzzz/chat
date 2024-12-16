from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from chat.models import Chat
from chat.serializers import ChatSerializer, ChatUserSerializer


# Create your views here.


class UserChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['created_at', 'username']
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class UserChatDetailView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatUserSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['created_at']


    def get_queryset(self):
        qs =super().get_queryset()
        token = self.kwargs['token']
        print(token)
        return  qs.prefetch_related('messages').filter(token=token)

