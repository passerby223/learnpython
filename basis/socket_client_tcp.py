# coding: utf-8 
# @Time    : 2020/3/13 上午12:36
# @File    : socket_client_tcp.py
# @Author  : wenbin
# @Software: PyCharm

import socket
s = socket.socket() # 创建客户套接字
s.connect(('127.0.0.1',8849))    # 尝试连接服务器
# s.send(b'hello!') # 向服务端发送信息
# s.send(b'hello!') # 向服务端发送信息会报错：TypeError: a bytes-like object is required, not 'str'
s.send(bytes('我是客户端', encoding='utf-8')) # 向服务端发送信息
ret = s.recv(1024)         # 对话(发送/接收)
print(ret.decode()) # 我是服务端
s.close()            # 关闭客户端套接字
