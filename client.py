import socket
import time
import threading


class Client:
    HOST = '127.0.0.1'
    PORT = 55555
    run = True

    def __init__(self, nick):
        self.nick = nick
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_client(self):
        self.client.connect((self.HOST, self.PORT))
        self.client.send(self.nick.encode('utf-8'))

    def print_msg(self):
        while self.run:
            try:
                msg = selfclient.recv(1024).decode('utf-8')
                if msg == 'NICK':
                    self.client.send(NICK.encode('utf-8'))
                elif msg == 'You were kicked from the server':
                    print(msg)
                    self.client.close()
                    self.run = False
                else:
                    print(msg)
            except Exception as e:
                print(f'Exception at reciving: {e}')
                self.client.close()
                break

    def send_msg(self):
        while self.run:
            try:
                msg = f'{NICK}: {input("")}'
                self.client.send(msg.encode('utf-8'))
            except Exception as e:
                print(f'Exception client send: {e}')
                break

    def run_client(self):
        self.connect_client()
        listen_thread = threading.Thread(target=self.print_msg)
        listen_thread.start()
        time.sleep(1)
        send_thread = threading.Thread(target=self.send_msg)
        send_thread.start()


if __name__ == '__main__':
    nick = input('Choose nick: ')
    client = Client(nick)
    client.run_client()
