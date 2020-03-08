# !/usr/bin/python3
# coding: utf-8 
# @Author  : wenbin
# @Time    : 2019/12/29 下午5:38
# @Software: PyCharm
# @File    : client.py
import zmq
# 创建zmq Context上下文类的实例
context = zmq.Context()
# 调用socket方法创建创建socket
socket = context.socket(zmq.REQ)
# 使用socket连接到服务端
socket.connect('tcp://localhost:12306')
print('zmq client start....')
socket.send_string('我准备好了,请给我发消息吧!')
message = socket.recv()
print('已经收到server端响应的信息: ', message.decode('utf-8'))
