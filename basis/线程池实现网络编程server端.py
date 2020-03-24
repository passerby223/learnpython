# coding: utf-8 
# @Time    : 2020/3/24 下午10:59
# @File    : 线程池实现网络编程server端.py
# @Author  : Always be conding
# @Software: PyCharm


import socket
from concurrent.futures import ThreadPoolExecutor

t_pool = ThreadPoolExecutor(max_workers=3)

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)


def comm(conn):
    while 1:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def serve():
    while 1:
        conn, addr = server.accept()
        t_pool.submit(comm, conn)
    server.close()

serve()