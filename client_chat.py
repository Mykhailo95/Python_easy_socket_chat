import socket
import threading
import os

s = socket.socket
host = '127.0.0.1'
port = 3000

def listen(s):
    while True:
        msg =  s.recv(2048)
        print(f"\r\r {msg.decode('ascii')}\n you: ", end='')


def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host,port))
 
    # для того чтобы слушать в фоне
    threading.Thread(target=listen,args=(s,), daemon=True).start()

    # говорим серверу что соед. с чатом
    s.send('__join'.encode('ascii'))

    # для бесконечного писание в чат
    while True:
        msg = input('my message: ')
        s.send(msg.encode('ascii'))

if __name__ == '__main__':
    # фвтомат очистка окна терминала и вывод приветсвия
    os.system('cls')
    print('Welcom to chat')
    connect(host, port)