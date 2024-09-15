import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PongConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'transcendence'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        player_id = data['player_id']
        player_y = data['player_y']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_update',
                'player_id': player_id,
                'player_y': player_y
            }
        )

    async def game_update(self, event):
        player_id = event['player_id']
        player_y = event['player_y']

        await self.send(text_data=json.dumps({
            'player_id': player_id,
            'player_y': player_y
        }))
