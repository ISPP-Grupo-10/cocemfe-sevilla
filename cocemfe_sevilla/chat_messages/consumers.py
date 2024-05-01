from django.utils import timezone
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from documents.models import Document
from professionals.models import Professional

from .models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_layer 
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        document_id = text_data_json["doc_id"]
        date = text_data_json["date"]
    
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
                "doc_id" : document_id ,
                "date": date,
            })
        
    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        document_id = event["doc_id"]
        date = event["date"]
        await create_message_from_websocket(username,message,document_id)
        await self.send(text_data = json.dumps({"message":message ,"username":username, "doc_id": document_id, "date": date}))
        
@sync_to_async
def create_message_from_websocket(username,message,document_id):
    author = Professional.objects.filter(username=username).get()
    content = message
    post_date = timezone.now()
    document = Document.objects.filter(pk=document_id).get()
    ChatMessage(author=author, content=content, post_date=post_date, document=document).save()
   
