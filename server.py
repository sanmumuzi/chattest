from socket import socket, AF_INET, SOCK_STREAM
import time
import threading


def echo_handle(address, client_sock):  # 处理
    print('Got connection from {}:{}'.format(address[0], address[1]))
    client_sock.send(b'Welcome!')
    while True:
        msg = client_sock.recv(1024)  # 如何让其避免发一句接一句--客户端多进程
        time.sleep(0.2)  # 不知是否能减小网络消耗？
        if not msg or msg == b'exit': break   # 如何让其可以发送空消息，又不引起无限循环呢
        print("{}:{} >>".format(address[0], address[1]), msg.decode('utf-8')) # 打印发送者
        for receiver in lists:  # 将所有同时连接者遍历
            if receiver['client'] != client_sock:  # 除自己外均要接收自己发送的消息
                receiver['client'].sendall(msg)
    client_sock.close()  # 关闭链接
    lists.remove({'client': client_sock, 'address': address})  # 将其从列表中移除
    print('Connection from {}:{} closed.'.format(address[0], address[1]))


def echo_server(address, backlog=5):  # 开启服务，同时监听5
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)  # 绑定
    sock.listen(backlog)   # 监听
    while True:
        client_sock, client_addr = sock.accept()  # 接受
        lists.append({'client': client_sock, 'address': client_addr}) # 按字典形式存入列表
        t = threading.Thread(target=echo_handle, args=(client_addr, client_sock))  # 多线程
        t.start()
        # echo_handle(client_addr, client_sock)

if __name__ == '__main__':
    lists = []
    echo_server(('', 20020))
    # 开启服务