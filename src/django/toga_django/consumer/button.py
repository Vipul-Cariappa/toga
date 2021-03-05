import json
from channels.generic.websocket import WebsocketConsumer


class ButtonConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        if action == "clicked":
            pass

        print("Got the Message From WebSocket")
