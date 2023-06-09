import socketio


sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.on('message')
def message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})
    print('emitted')


@sio.on('vibrate')
def handle_vibrate(data):
    print('got vibrate')


@sio.event
def disconnect():
    print('disconnected from server')


def init():
    sio.connect('http://127.0.0.1:8000')


def close():
    # sio.close()
    pass


def emit_message(msg):
    sio.emit('message', msg)


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
        emit_message(data)
