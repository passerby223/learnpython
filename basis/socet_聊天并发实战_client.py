# coding: utf-8 
# @Time    : 2020/3/15 下午10:52
# @File    : socet_聊天并发实战_client.py
# @Author  : wenbin
# @Software: PyCharm

from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    msg=input('>>: ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    msg_recv=client.recv(1024)
    print(msg_recv.decode('utf-8'))