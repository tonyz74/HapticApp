import socketio
import input
import events as ev


sio = socketio.Client()
is_connected = False


class Messenger:
    def init():
        sio.connect("http://127.0.0.1:8000")

    def is_connected() -> bool:
        return is_connected

    @sio.event
    def connect():
        global is_connected
        print("[messenger] successfully connected to server.")
        input.event_loop.post_notif(ev.MESSENGER_CONNECTED, None)
        is_connected = True

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
        input.event_loop.post_notif(ev.MESSENGER_DISCONNECTED, None)
        print("[messenger] disconnected from server.")

    def emit_message(msg):
        if not is_connected:
            print("[messenger] cannot send message, not connected.")
            return
        sio.emit("message", msg)

    def close():
        if not is_connected:
            print("not disconnecting")
            return

        sio.disconnect()
