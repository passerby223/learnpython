# coding: utf-8 
# @Time    : 2020/3/24 下午11:04
# @File    : 线程池实现网络编程client端.py
# @Author  : Always be conding
# @Software: PyCharm

'''
client端
'''
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))

while 1:
    msg = input('>>>').strip()
    if not msg: continue
    client.send(msg.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))

client.close()
