# coding: utf-8 
# @Time    : 2020/3/13 上午12:50
# @File    : socket_server_udp.py
# @Author  : wenbin
# @Software: PyCharm

import socket
while True:
    udp_s = socket.socket(type=socket.SOCK_DGRAM) # 创建一个服务器的套接字
    # udp_s.bind(('127.0.0.1', 8849))
    udp_s.bind(('localhost', 8849))
    msg,addr = udp_s.recvfrom(1024)
    print(msg.decode(), '|', addr) # 我是客户端哈 | ('127.0.0.1', 34997)
    udp_s.sendto(bytes('我是服务端啊', encoding='utf-8'), addr)
    udp_s.close()