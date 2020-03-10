import socket
from flask import make_response, request, abort
from functools import wraps

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'haproxy' and auth.password == 'haproxy':
            return f(*args, **kwargs)

        return make_response('Login and password required!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

    return decorated

def filter_cicd(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if request.remote_addr == "192.168.9.70":
            return f(*args, **kwargs)
        else:
            return abort(403)

    return wrapped

def executeCommand(commandToSend):
    socket_open = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    socket_open.settimeout(1)
    socket_open.connect('/run/haproxy/admin.sock')
    socket_open.send(str.encode(commandToSend))
    file_handle = socket_open.makefile()
    data = file_handle.read().splitlines()
    socket_open.close()
    return '\n'.join(data)

