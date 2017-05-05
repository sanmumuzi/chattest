from socket import socket, AF_INET, SOCK_STREAM
import threading, time
from tkinter import *  # 直接使用，但是个人感觉可能产生冲哭
# import tkinter as tk  ## 每次使用都需要加tk.xxx

s = socket(AF_INET, SOCK_STREAM)
# s.connect(('127.0.0.1', 20014))
s.connect(('120.25.242.228', 20020))

root = Tk()
text = Text(root)
# text.insert(INSERT, "hello......")
text.insert(END, "hello.........this is tkinter GUI.")
text.grid(row=0, columnspan=15)

# text['state'] = NORMAL
# text.insert(END, '\n' + '123')
# text['state'] = DISABLED

userLable = Label(root, text='UserName')
userLable.grid(row=1)

userInput = Entry(root)
userInput.grid(row=1, column=1, columnspan=8)

messageLabel = Label(root, text="Message")
messageLabel.grid(row=2)

messageInput = Entry(root)
messageInput.grid(row=2, column=1, columnspan=8)


def postMessage():  # 不能改变这个名字
    text['state'] = NORMAL
    text.insert(END, '\n' + userInput.get() + ":" + messageInput.get())
    temptext = userInput.get() + ":" + messageInput.get()
    textgo = bytes(temptext, encoding='utf-8')
    s.sendall(textgo)
    text['state'] = DISABLED

postMessageBtn = Button(root, text='POST', command=postMessage)
postMessageBtn.grid(row=2, column=9)


def receive():
    while True:
        temp = s.recv(1024)
        if temp:
            text['state'] = NORMAL
            text.insert(END, '\n' + temp.decode('utf-8'))
            text['state'] = DISABLED
        time.sleep(0.2)
t = threading.Thread(target=receive)
t.daemon = True
t.start()

root.mainloop()










