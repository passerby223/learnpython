# coding: utf-8 
# @Time    : 2020/3/19 下午12:56
# @Software: PyCharm
# @File    : 多线程实现socket_client.py

import socket
import threading

'''
多线程实现socket-client
'''

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8080))


while True:
    msg = input('输入内容>>>').strip()
    if not msg: continue
    c.send(bytes(msg, encoding='utf-8'))
    data = c.recv(1024)
    print(data.decode())
