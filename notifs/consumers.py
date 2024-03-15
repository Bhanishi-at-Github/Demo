'''
    Consumers file for the notifications
'''

import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    '''
    Consumer class for the notifications
    '''
    # pylint: disable=attribute-defined-outside-init
    async def connect(self):
        self.group_name = 'public_room'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
        self.group_name,
        self.channel_name
    )

    async def send_notification(self, event):
        '''
        Class to send notification
        '''
        await self.send(text_data=json.dumps({ 'message': event['message'] }))
