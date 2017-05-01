# a = input(">>")
# print(a)
# b = bytes(a, encoding='utf-8')
# print(b)
# print(type(b))


from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('120.25.242.228', 20010))
while True:
    print(s.recv(1024))
    word = input('>>')
    word = bytes(word, encoding='utf-8')
    s.sendall(word)
    if word == b'exit': break
print('The session is over.')

