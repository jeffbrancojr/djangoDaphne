from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    #groups = ["broadcast"]

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        print(self.scope)
        await self.accept()
        await self.send("connected")
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        #await self.accept("subprotocol")
        # To reject the connection, call:
        #await self.close()

    async def receive(self, text_data, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        print(text_data)
        received_text=text_data
        await self.send(received_text)
        # await self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # await self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        #await self.close()
        # Or add a custom WebSocket error code!
        #await self.close(code=4123)

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass