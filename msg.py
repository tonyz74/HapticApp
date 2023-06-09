import socketio


sio = socketio.Client()


class Messenger:
    def init():
        sio.connect("http://127.0.0.1:8000")

    @sio.event
    def connect():
        print("Connected to server.")

    @sio.on("message")
    def message(data):
        print("Message received with ", data)
        sio.emit("my response", {"response": "my response"})

    @sio.on("vibrate")
    def handle_vibrate(data):
        print("received confirmation of vibrate")

    @sio.event
    def disconnect():
        print("disconnected")

    def emit_message(msg):
        sio.emit("message", msg)

    def send_vibrate(data):
        example_format = {
                # in format [VIBRATE, PAUSE, VIBRATE, PAUSE...]
                "pattern": [100, 400, 100],
                "interval": 2000
        }

        if data is None:
            print("HELP:")
            print(example_format)
        else:
            Messenger.emit_message(data)
