# coding: utf-8 
# @Time    : 2020/3/13 上午12:51
# @File    : socket_client_udp.py
# @Author  : wenbin
# @Software: PyCharm

import socket
ip_address = ('localhost', 8849)
socket_udp_client = socket.socket(type=socket.SOCK_DGRAM)
socket_udp_client.sendto(bytes('我是客户端哈', encoding='utf-8'), ip_address)
recv_msg, addr = socket_udp_client.recvfrom(1024)
print(recv_msg.decode(), '|', addr) # 我是服务端啊 | ('127.0.0.1', 8849)