import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

user=get_user_model()

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):

        print('connected', event)
        await self.send({
            'type':'websocket.accept',
            'message':'welcome',
        })
    async def websocket_receive(self,event):
        print('recieved', event)
    async def websocket_disconnect(self,event):
        print('disconnected', event)