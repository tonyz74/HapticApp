from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '963247'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print("connect")

@socketio.on('message')
def handle_message(msg):
    print("got message. Content: ", msg)
    emit('vibrate', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=8000)
