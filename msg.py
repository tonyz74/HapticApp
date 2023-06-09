import socketio


sio = socketio.Client()
finished_init = False


class Messenger:
    def init():
        global finished_init

        sio.connect("http://127.0.0.1:8000")
        finished_init = True

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
        if not finished_init:
            print("Not connected yet!")
            return
        sio.emit("message", msg)

    def close():
        if not finished_init:
            return

        sio.disconnect()
