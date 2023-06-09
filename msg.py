import socketio


sio = socketio.Client()
is_connected = False


class Messenger:
    def init():
        global is_connected

        sio.connect("http://127.0.0.1:8000")
        is_connected = True

    def is_connected() -> bool:
        return is_connected

    @sio.event
    def connect():
        print("[messenger] successfully connected to server.")

    @sio.on("message")
    def message(data):
        raise Exception("Why is this being called?")

    @sio.on("vibrate")
    def handle_vibrate(data):
        print("[messenger] confirmed that vibration has been received.")

    @sio.event
    def disconnect():
        global is_connected
        is_connected = False
        print("[messenger] disconnected from server.")

    def emit_message(msg):
        if not is_connected:
            print("[messenger] cannot send message, not connected.")
            return
        sio.emit("message", msg)

    def close():
        if not is_connected:
            return

        sio.disconnect()
