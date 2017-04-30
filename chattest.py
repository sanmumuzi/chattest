import socket, threading, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 9999
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from {}:{}...'.format(addr[0], addr[1]))
    sock.send(b'Welcome!!!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data and data.decode('utf-8') == 'exit': break
        sock.send('Hello, {}'.format(data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from {}:{}'.format(addr[0], addr[1]))

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
