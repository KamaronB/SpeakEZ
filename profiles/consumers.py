import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Room,Message


#make chat consumer class that inherits from AsyncConsumer
class ChatConsumer(AsyncConsumer):

        async def websocket_connect(self,event):
            print("connected",event)
            room_name=self.scope['url_route']['kwargs']['room_name']
            current_user=self.scope['user']
            other_user,messages= await self.get_room(room_name)
            print(current_user,other_user,messages)
            # await executes code and waits for it to finish
            await self.send({
            "type": "websocket.accept"
            })

            # await asyncio.sleep(19)
            # await self.send({
            # "type": "websocket.send",
            # "text": "Hello World",
            # })





        async def websocket_receive(self, event):
            print("recieve",event)

        async def websocket_disconnect(self,event):
            print("disconnected",event)





        #asynchronously get the current room
        @database_sync_to_async
        def get_room(self,room_name):
         room= Room.objects.get(room_name=room_name)
         other_user= room.user_2
         messages = reversed(room.messages.order_by('-timestamp')[:50])

         return other_user,messages
