from channels.consumer import SyncConsumer


class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        }
        )
        print(f'connected to {event}: {self}')

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
        print('received text')

    def websocket_disconnect(self, event):
        self.send({
            "type": "websocket.disconnect",
        })

