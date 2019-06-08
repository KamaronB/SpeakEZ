import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from .models import Room,Message


#make chat consumer class that inherits from AsyncConsumer
class ChatConsumer(AsyncConsumer):

        async def ws_connect(self,event):
            print("connected",event)
            #await executes code and waits for it to finish 
            await self.send({
            "type": "websocket.accept"
            })


        async def ws_disconnect(self,event):
            print("disconnected",event)


        async def ws_receive(self, event):
            print("recieved",event)
