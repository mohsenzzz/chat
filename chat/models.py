from django.db import models

from user.models import User


# Create your models here.

class Chat(models.Model):
    token=models.CharField(max_length=100,unique=True)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.token}' or "unknown"



    @classmethod
    def get_chat(cls,token,user):
        """
        get chat token and user
        if chat with token does not exist, create it and add current user to it
        else if chat with token exist, and current user did not add to it add current user
        and then return chat object
        :param token:
        :param user:
        :return:
        """
        chat = cls.objects.prefetch_related('user').filter(token=token).first()

        if chat is None:
            chat = cls.objects.create(token=token)
            chat.user.add(user)
        elif chat.user.filter(id=user.id).first() is None:
            chat.user.add(user)

        return chat



class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    @classmethod
    def create_msg(cls, chat, sender, content):
        return cls.objects.create(chat=chat,sender=sender,content=content)
