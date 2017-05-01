# import requests
# url = 'http://httpbin.org/post'
#
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
#
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
#
# resp = requests.post(url, data=parms, headers=headers)
# text = resp.text
# print(text)

# import requests
#
# resp = requests.head('http://www.python.org/index.html')
# status = resp.status_code
# print(status)
# print(type(resp.headers))
# for x, y in resp.headers.items():
#     print(x, y)
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
# content_length = resp.headers['content-length']
# print(last_modified)
# print(content_type)
# print(content_length)

# import requests
# resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user', 'password'))
# resp2 = requests.get('http://pypi.python.org/pypi?:action=login', cookies=resp.cookies)

# import requests
# url = 'http://httpbin.org/post'
# files = {'file': ('data.csv', open('data.csv', 'rb'))}
# r = requests.post(url, files=files)

# import requests
# r = requests.get('http://httpbin.org/get?name=Dave&n=37',
#                  headers={'User-agent': 'goaway/1.0'})
# resp = r.json()
# print(resp['headers'])
# print(resp['args'])

# from socketserver import BaseRequestHandler, TCPServer
#
# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('Got connection from', self.client_address)
#         while True:
#
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)
#
# if __name__ == '__main__':
#     serv = TCPServer(('', 23335), EchoHandler)
#     serv.serve_forever()



# from socketserver import BaseRequestHandler, TCPServer
#
# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('Got connection from', self.client_address)
#         while True:
#             msg = self.request.recv(8192)  # 把发过来的再发回去，interesting
#             if not msg:
#                 break
#             self.request.send(msg)
#
# if __name__ == '__main__':
#     serv = TCPServer(('', 23336), EchoHandler)
#     serv.serve_forever()

# from socketserver import StreamRequestHandler, ThreadingTCPServer, TCPServer
#
# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print('Got connection from:', self.client_address)
#         for line in self.rfile:
#             self.wfile.write(line)
#
# # if __name__ == '__main__':
# #     serv = ThreadingTCPServer(('', 20001), EchoHandler)  # 有可能被无限恶意攻击
# #     serv.serve_forever()
#
# if __name__ == '__main__':
#     from threading import Thread
#     NWORKERS = 16
#     serv = TCPServer(('', 20002), EchoHandler)
#     for n in range(NWORKERS):
#         t = Thread(target=serv.serve_forever())
#         t.daemon = True
#         t.start()
#     serv.serve_forever()

# import socket
# from socketserver import StreamRequestHandler
#
# class EchoHandler(StreamRequestHandler):
#     timeout = 5
#     rbufsize = -1
#     wbufsize = 0
#     disable_nagle_algorithm = False
#     def handle(self):
#         print('Got connection from:', self.client_address)
#         try:
#             for line in self.rfile:
#                 self.wfile.write(line)
#         except socket.timeout:
#             print('Timed out!----fuck!!!')
#

from socket import socket, AF_INET, SOCK_STREAM
import time
import threading

def echo_handle(address, client_sock):
    print('Got connection from {}:{}'.format(address[0], address[1]))
    client_sock.send(b'Welcome!')
    while True:
        msg = client_sock.recv(1024)
        # time.sleep(1)
        if not msg or msg == b'exit': break
        client_sock.sendall(msg)
    client_sock.close()
    print('Connection from {}:{} closed.'.format(address[0], address[1]))

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        t = threading.Thread(target=echo_handle, args=(client_addr, client_sock))
        t.start()
        # echo_handle(client_addr, client_sock)

if __name__ == '__main__':
    echo_server(('', 20010))