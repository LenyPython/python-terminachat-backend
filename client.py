import socket
import time
import threading

HOST = '127.0.0.1'
PORT = 55555
NICK = ''


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(NICK.encode('utf-8'))


def print_msg():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICK':
                client.send(NICK.encode('utf-8'))
            else:
                print(f'{msg}')
        except Exception as e:
            print(f'Exception at reciving: {e}')
            client.close()
            break


def send_msg():
    while True:
        try:
            msg = f'{NICK}: {input("")}'
            client.send(msg.encode('utf-8'))
        except Exception as e:
            print(f'Exception client send: {e}')
            break


def main():

    listen_thread = threading.Thread(target=print_msg)
    listen_thread.start()
    time.sleep(1)
    send_thread = threading.Thread(target=send_msg)
    send_thread.start()


if __name__ == '__main__':
    NICK = input('Choose nick: ')
    main()
