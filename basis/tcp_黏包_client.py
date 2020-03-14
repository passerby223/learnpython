# coding: utf-8 
# @Time    : 2020/3/14 下午4:08
# @File    : tcp_黏包_client.py
# @Author  : wenbin
# @Software: PyCharm


import socket
BUFSIZE=1024
ip_port=('127.0.0.1',8888)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(ip_port)
while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break
    # s.send(msg.encode('utf-8'))
    s.send(bytes(msg, encoding='utf-8'))
    act_res=s.recv(BUFSIZE)
    print(act_res.decode('utf-8'),end='')