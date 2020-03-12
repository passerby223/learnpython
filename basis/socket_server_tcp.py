# coding: utf-8 
# @Time    : 2020/3/13 上午12:28
# @File    : socket_server_tcp.py
# @Author  : wenbin
# @Software: PyCharm

import socket
from socket import SOL_SOCKET,SO_REUSEADDR
''' 
套接字(socket)初使用
3.1 基于TCP协议的socket
tcp是基于连接的，必须先启动服务端，然后再启动客户端去连接服务端

server端：
如果报错：OSError: [Errno 98] Address already in use解决方法：
# 加入一条socket配置，重用ip和端口
'''
while 1:
    s = socket.socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 加入一条socket配置，重用ip和端口
    s.bind(('127.0.0.1', 8849)) # 把地址绑定到套接字
    s.listen() # 监听连接
    conn,addr = s.accept() #接受客户端链接
    ret = conn.recv(1024)  #接收客户端信息
    print(ret.decode())       #打印从客户端接收到的信息：我是客户端
    # conn.send(b'hi')        # 向客户端发送信息
    conn.send(bytes('我是服务端', encoding='utf-8'))        # 向客户端发送信息,会报错：TypeError: a bytes-like object is required, not 'str'
    conn.close()       # 关闭客户端套接字
    s.close()        # 关闭服务器套接字(可选)
