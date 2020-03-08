import socket

def executeCommand(commandToSend):
    socket_open = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    socket_open.settimeout(1)
    socket_open.connect('/run/haproxy/admin.sock')
    socket_open.send(str.encode(commandToSend))
    file_handle = socket_open.makefile()
    data = file_handle.read().splitlines()
    socket_open.close()
    return '\n'.join(data)

