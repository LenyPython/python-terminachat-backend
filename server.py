import socket
import threading

serv = socket.socket(socket.Af_NET, socket.SOCK_STREAM)

ADDRESS = '127.0.0.1'
PORT = 12121

clients = dict()

serv.bind((ADDRESS, PORT))
serv.listen()


def send_to_all(msg):
    for client in clients:
        serv.send(msg.encode('utf-8'))


def hear_and_send(client):
    while True:
        try:
            msg = serv.recv(1024)
            broadcast(msg)
        except Exception as e:
            user, nick = clients.pop(client)
            user.close()
            broadcast(f'User {nick} lef the chat')
            print(f'Exception occured: {e}')
            break


while True:
    try:
        client, address = serv.accept()
        client.send(f'Welcome {client}, you have connected'.encode('utf-8'))
    except Exception as e:
        print('Error occured: ')
        print(e)
