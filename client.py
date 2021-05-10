import socket
import threading

NICK = input('Choose nick: ')
HOST =
PORT =
client = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(NICK.encode('utf-8'))


while True:
    msg = client.recv()
    if len(msg) < 1:
        break
    print(msg.decode('utf-8'))

client.close()
