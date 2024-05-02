from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("alert", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alert", self.channel_name)

    async def receive(self, text_data):
        pass

    async def alert_message(self, event):
        message = event['message']
        data = event['data']
        await self.send(text_data=json.dumps({
            'message': message,
            'data': data
        }))