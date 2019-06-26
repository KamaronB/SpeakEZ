import asyncio
import json
import cv2
import numpy as np
import base64
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Room,Message


#make chat consumer class that inherits from AsyncConsumer
class ChatConsumer(AsyncConsumer):

        async def websocket_connect(self,event):
            print("connected",event)

            #get the name of the chatroom
            room_name=self.scope['url_route']['kwargs']['room_name']
            #get the User
            current_user=self.scope['user']

            #get the messages and the other userid
            other_user,messages= await self.get_room(room_name)

            #create chat room for two users using channels_redis and the room_name
            chat_room= f"room_{room_name}"
            self.chat_room= chat_room
            await self.channel_layer.group_add(
                chat_room,
                self.channel_name
            )

            # await executes code and waits for it to finish
            await self.send({
            "type": "websocket.accept"
            })



            # await asyncio.sleep(19)





        async def websocket_receive(self, event):
            # print("recieve",event)
            user=self.scope['user']
            username= user.username
            userid= user.id
            #grab data sent from room.html onopen function
            #example recieve {'type': 'websocket.receive', 'text': '{"message":"ads"}'}
            text_data= event.get('text',None)
            #if there is text
            if text_data is not None:
                #save the dictionary sent inside of text_data
                data_dict = json.loads(text_data)

                ##get the actual message from data_dict
                msg=data_dict.get('message')
                vid=data_dict.get('video')


                #Response data
                if msg is not None:
                    response= {
                    "msg":msg,
                    "username": username,


                        }
                    #save message to database
                    await self.save_message(msg)
                else:

                     response={
                    'video': vid,
                    'userid': userid,

                        }




                #broadcasts the message event to be sent
                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                    #the chat message function created earlier
                    "type": "chat_message",
                    "text": json.dumps(response)
                    }
                )


        async def websocket_disconnect(self,event):
            print("disconnected",event)



        async def chat_message(self,event):
            #sends the actual message
            # print('message',event)
            await self.send({
            "type": "websocket.send",
            "text": event['text']
            })




        #asynchronously get the current room
        @database_sync_to_async
        def get_room(self,room_name):
         room= Room.objects.get(room_name=room_name)
         other_user= room.user_2
         messages = reversed(room.messages.order_by('-timestamp')[:50])

         return other_user,messages



        # #asynchronously save messages to the database
        @database_sync_to_async
        def save_message(self,msg):
         name= room_name=self.scope['url_route']['kwargs']['room_name']
         current_room=Room.objects.get(room_name=name)
         user=self.scope['user']
         return Message.objects.create(room=current_room,handle=user.username,message=msg)
