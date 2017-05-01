# a = input(">>")
# print(a)
# b = bytes(a, encoding='utf-8')
# print(b)
# print(type(b))


from socket import socket, AF_INET, SOCK_STREAM
import threading, time
s = socket(AF_INET, SOCK_STREAM)
s.connect(('120.25.242.228', 20011))
# s.connect(('127.0.0.1', 20011))

# while True:
#     print(s.recv(1024))
#     word = input()
#     word = bytes(word, encoding='utf-8')
#     s.sendall(word)
#     if word == b'exit': break
# print('The session is over.')


def receive():  # 接收服务器端的数据
    while True:
        temp = s.recv(1024)
        if temp:
            print(temp.decode('utf-8'))  # 解码为utf-8
        time.sleep(0.2)  # 每0.2s进行一次信息接收


def scan():  # 发送信息
    while True:
        word = input()
        words = bytes(word, encoding='utf-8')  # 变换为字节串
        s.sendall(words)
        if words == b'exit': break  # exit退出
    print('The session is over.')

if __name__ == '__main__':
    t = threading.Thread(target=receive)  # 开启一个线程给接收函数
    t.daemon = True  # 守护进程，当程序结束时，线程结束
    t.start()
    scan()


# 1。这样使用线程行不
# 2。编码问题，输出非中文
# 3.输入信息时，被输出信息顶掉 ---
# 4.中断后无限接收的问题 --- 解决:守护进程
# 5. # 如何让其可以发送空消息，又不引起无限循环呢
# 6. 是在客户端用两个命令行，两个py文件？一个接收，一个发送？