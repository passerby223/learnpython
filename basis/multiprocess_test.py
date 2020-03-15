# coding: utf-8 
# @Time    : 2020/3/15 下午6:32
# @File    : multiprocess_test.py
# @Author  : wenbin
# @Software: PyCharm
import time
import os
from multiprocessing import Process

'''
1. multiprocess模块
仔细说来，multiprocess不是一个模块而是python中一个操作、管理进程的包。 之所以叫multi是取自multiple的多功能的意思,在这个包中几乎包含了和进程有关的所有子模块。由于提供的子模块非常多，为了方便大家归类记忆，我将这部分大致分为四个部分：创建进程部分，进程同步部分，进程池部分，进程之间数据共享。

1.1 multiprocess.process模块
1.1.1 process模块介绍
process模块是一个创建进程的模块，借助这个模块，就可以完成进程的创建。

Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

强调：
1. 需要使用关键字的方式来指定参数
2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

参数介绍：
group参数未使用，值始终为None
target表示调用对象，即子进程要执行的任务
args表示调用对象的位置参数元组，args=(1,2,'egon',)
kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}
name为子进程的名称

方法介绍：

p.start()：启动进程，并调用该子进程中的p.run()

p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法

p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁

p.is_alive():如果p仍然运行，返回True

p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程

属性介绍：

p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置

p.name:进程的名称

p.pid：进程的pid

p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)

p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）

在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。因此如果将process()直接写在文件中就会无限递归创建子进程报错。所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候 ，就不会递归运行了。

1.1.2 使用process模块创建进程
在一个python进程中开启子进程，start方法和并发效果。
'''

# def f(name):
#     print('hello', name)
#     print('我是子进程')
#
#
# p = Process(target=f, args=('Jack',))
# p.start()
# time.sleep(1)
# print('执行主进程的内容了')

'''
join方法
'''
# print('分割线'.center(50, '*'))
#
#
# def f1(name):
#     print('hello', name)
#     time.sleep(1)
#     print('我是子进程')
#     print('子进程执行结束')
#     time.sleep(1)
#
#
# p = Process(target=f1, args=('bob',))
# p.start()
# p.join()
# print('我是父进程')

'''
查看主进程和子进程的进程号
'''
# print('分割线'.center(50, '*'))
#
#
# def f2(x):
#     print('子进程id ：', os.getpid(), '父进程id ：', os.getppid())
#     print('x*x:', x * x)
#
#
# print('主进程id ：', os.getpid())
# for i in range(5):
#     p = Process(target=f2, args=(i,))
#     p.start()

'''
进阶，多个进程同时运行（注意，子进程的执行顺序不是根据启动顺序决定的）
多个进程同时运行：
'''
# time.sleep(1)
# print('分割线'.center(50, '*'))
#
#
# def f3(name):
#     print('hello', name)
#     print('子进程id ：', os.getpid())
#     time.sleep(1)
#
#
# p_lst = []
# p_pid_list = []
# for i in range(5):
#     p = Process(target=f3, args=('Lucy',))
#     p.start()
#     p_lst.append(p)
#
# print('p_lst:', p_lst)


# print('分割线'.center(50, '*'))
#
#
# def f4(name):
#     print('hello', name)
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(5):
#         p = Process(target=f4, args=('bob',))
#         p.start()
#         p_lst.append(p)
#         p.join()
#     print([p.join() for p in p_lst])
#     print('父进程在执行')


'''
进程之间的数据隔离问题
'''

# def work():
#     global n
#     n = 0
#     print('子进程内: ', n)
#
#
# if __name__ == '__main__':
#     n = 100
#     p = Process(target=work)
#     p.start()
#     print('主进程内: ', n)

'''
守护进程
会随着主进程的结束而结束。
主进程创建守护进程：
1.守护进程会在主进程代码执行结束后就终止
2.守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止
守护进程的启动：
'''

# class Myprocess(Process):
#     def __init__(self, person):
#         super().__init__()
#         self.person = person
#
#     def run(self):
#         print(os.getpid(), self.name)
#         print('%s正在和女主播聊天' % self.person)
#
#
# p = Myprocess('哪吒')
# p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
# p.start()
# time.sleep(10)  # 在sleep时查看进程id对应的进程ps -ef|grep id
# print('主')

'''
主进程代码执行结束守护进程立即结束
'''


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1 = Process(target=foo)
p2 = Process(target=bar)
# p1是守护进程,p2不是守护进程
p1.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
p1.start()
p2.start()
time.sleep(0.1)
# 打印该行则主进程代码结束,则守护进程p1应该被终止.
# 可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.
print("main-------")
