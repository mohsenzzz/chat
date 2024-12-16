from django.db.models import Q
from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated



from chat.models import Chat
from chat.serializers import ChatSerializer, ChatUserSerializer



# Create your views here.





class UserChatListView(ListAPIView):
    """
    list all users that user chats with them
    user can search users by username or phone_number
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username','user__phone_number']
    ordering_fields = ['created_at']
    def get_queryset(self):
        qs = super().get_queryset()
        print(self.request.user.id)


        return qs.filter(user__id=self.request.user.id)


class UserChatDetailView(ListAPIView):
    """
    get chat detail by chat token
    """
    queryset = Chat.objects.all()
    serializer_class = ChatUserSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['created_at']


    def get_queryset(self):
        qs =super().get_queryset()
        token = self.kwargs['token']
        print(token)
        return  qs.prefetch_related('messages').filter(token=token)

