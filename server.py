import eventlet
import socketio
import tinydb

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


db = tinydb.TinyDB('db.json')


@sio.event
def connect(sid, environ):
    sio.emit("chat", db.all(), to=sid)


@sio.event
def message(sid, data):
    sio.emit("message", data)
    db.insert(data)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
