# coding: utf-8 
# @Author  : wenbin
# @Time    : 2020/3/19 下午12:55
# @Software: PyCharm
# @File    : 多线程实现socket_server.py

import socket
import threading

'''
多线程实现socket-server
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(5)


def action(conn):
    while True:
        data = conn.recv(1024)
        print(data)
        conn.send(data.upper())


if __name__ == '__main__':

    while True:
        conn, addr = s.accept()

        p = threading.Thread(target=action, args=(conn,))
        p.start()
