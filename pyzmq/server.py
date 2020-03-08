# !/usr/bin/python3
# coding: utf-8 
# @Author  : wenbin
# @Time    : 2019/12/29 下午5:25
# @Software: PyCharm
# @File    : server.py.py
import zmq
import queue
# 创建zmq Context上下文类的实例
context = zmq.Context()
# 调用socket方法创建创建socket
socket = context.socket(zmq.REP)
# 给socket绑定服务器server端ip地址并指定端口号
socket.bind('tcp://*:12306')

# 创建一个用来存储压测流量的队列
data_queue = queue.Queue()
# 打开流量文件,把文件中的流量存到queue里
with open('traffic') as file:
    for i in file:
        data_queue.put_nowait(i.strip('\n'))
print('zmq server start....')
while True:
    message = socket.recv()
    print('我是server端，收到了client端发来的消息: ', message.decode('utf-8'))
    print('开始发送数据到client端......')
    single_data = data_queue.get()
    socket.send_string(single_data)
    data_queue.put(single_data)
    print('向client端发送数据完毕!')
