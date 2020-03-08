# !/usr/bin/python3
# coding: utf-8 
# @Author  : wenbin
# @Time    : 2019/12/29 下午2:35
# @Software: PyCharm
# @File    : client.py
import socket

# 创建socket对象
s = socket.socket()
# 连接远程服务器
s.connect(('10.118.47.46', 12306))
# 打印出server端发来的message
print('message from server: ', s.recv(1024).decode('utf-8'))
# 关闭socket连接
s.close()