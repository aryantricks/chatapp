from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

messages = []


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@socketio.on('message')
def handle_message(data):
    messages.append(data)
    socketio.emit('update_chat', messages)
