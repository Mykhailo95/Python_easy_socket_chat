import socket

host = '127.0.0.1'
port = 3000

def listen(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))
    print(f'Listening at {host}:{port}')

    numbers = []
    while True:
        msg, addr = s.recvfrom(2048)

        if addr not in numbers:
            numbers.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        if msg.decode('ascii') == '__join':
            print(f'Clinet {client_id} joined chat')
            continue

        msg = f'client{client_id}: {msg.decode("ascii")}'
        for number in numbers:
            if number == addr:
                continue

            s.sendto(msg.encode('ascii'), number)
    

if __name__ == '__main__':
    listen(host, port)