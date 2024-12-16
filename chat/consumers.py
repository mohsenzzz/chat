from channels.generic.websocket import AsyncWebsocketConsumer
import json

from .models import Chat, Message

from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    def create_chat(self,token,user):
        chat = Chat.objects.get_or_create(token=token,user=user)
        return chat
    async def connect(self):
        """
        if user is authenticated  then create websocket connection and save chat info in database
        :return:
        """
        user = self.scope["user"]
        if user.is_authenticated:
            print("ok")
            self.token= self.scope['url_route']['kwargs']['token']
            self.user = self.scope['user']

            self.chat = await database_sync_to_async(Chat.get_chat)(self.token, self.user)

            await self.channel_layer.group_add(self.token, self.channel_name)

            await self.accept()




    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.token, self.channel_name)


    async def receive(self, text_data):
        data= json.loads(text_data)
        message = data['message']
        new_message=await database_sync_to_async(Message.create_msg)(self.chat,self.user,message)
        await self.channel_layer.group_send(self.token, {
            'type': 'chat_message',
             'message': message
        })

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            "message": message
        }))