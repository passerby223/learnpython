# coding: utf-8 
# @Author  : wenbin
# @Time    : 2020/3/16 上午11:04
# @Software: PyCharm
# @File    : multiprocess_Process.py


from multiprocessing import Process

import time
import random
import os
import sys

''' 
使用process模块创建进程
'''

# def task(name, msg):
#     print('{}{}'.format(name, msg))
#     print('{} is running!'.format(name))
#     time.sleep(2)
#     print('{} is done!'.format(name))
#
#
# # 以位置参数进行传参，位置参数需要放到一个元组中
# p = Process(target=task, args=('task1', '进程已成功启动!'))
# # 以关键字参数进行传参，关键字参数需要放到一个字典dict中
# p1 = Process(target=task, kwargs={'name': 'task2', 'msg': '进程已成功启动!'})
# # 以关键字参数进行传参时，如果形参与task方法中的形参变量名不一致会报错：TypeError: task() got an unexpected keyword argument 'name1'
# # p2 = Process(target=task, kwargs={'name1': 'task3', 'msg': '进程已成功启动!'})
# p.start() # 启动进程
# p1.start() # 启动进程
# print(p.is_alive())  # 如果p仍然运行，返回True,否则返回false
# print(p1.is_alive())
# # p2.start() # 启动进程
# print(p.pid) # 打印进程4的PID
# print(p1.pid) # 打印进程的PID
# # print(p2.pid) # 打印进程的PID
# time.sleep(10) # 休眠以便使用'ps -elf | grep PID  | grep -v grep'可以查看到该进程
# print(p.is_alive())
# print(p1.is_alive())
# print('程序结束'.center(10, '-'))

'''
打印：
17727
17728
task1进程已成功启动!
task1 is running!
task2进程已成功启动!
task2 is running!
task1 is done!
task2 is done!
---程序结束---
'''

''' 
打印主进程id 及子进程id2
'''
# def task1():
#     print('task1 is running!')
#     """
#     os.getppid()
#     Return the parent's process id.
#
#     If the parent process has already exited, Windows machines will still
#     return its id; others systems will return the id of the 'init' process (1).
#     """
#     """
#     os.getpid()
#     Return the current process id.
#     """
#     print('子进程id：{}, 父进程id：{}'.format(os.getpid(), os.getppid()))
#     print('task1 is done!')
#
# print('主进程id ：', os.getpid())
# p = Process(target=task1)
# p.start()
# print('主进程 is done!')

''' 
再启动多个进程看一下，运行的效果：(注意，子进程的执行顺序不是根据启动顺序决定的)
'''

# def task(name):
#     print('{} is running!'.format(name))
#     time.sleep(3)
#     print('{} is done!'.format(name))
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=task, args=(i, ))
#         p.start()
#     print('--- 主进程 ----')

'''
进程间的数据隔离
进程的运行时数据是互相独立的，不会相互影响。
'''
# x = 100
#
#
# def change():
#     global x
#     x = 10
#     print('子进程修改了x,子进程结束了！')
#
#
# if __name__ == '__main__':
#     p = Process(target=change)
#     p.start()
#     time.sleep(5)  # 想办法等子进程结束 此处应该有思考
#     print(x) # 100 从例子中可以看到，父进程中的X变量并没有被子进程中的代码修改掉。

''' 
join
接下来我们看一下上面代码中的问题，也就是我们应该如何优雅的实现父进程等待子进程结束呢？
这里就用到了Python中进程对象的join()。
'''
# x = 100
#
#
# def change():
#     global x
#     x = 10
#     print('子进程修改了x,子进程结束了！')
#
#
# if __name__ == '__main__':
#     p = Process(target=change)
#     p.start()
#     p.join()  # 优雅地实现主进程等待子进程结束
#     print(x)

'''
再来几个多线程的例子，验证一下：
'''

# def task(n):
#     print('这是子进程:{}'.format(n))
#     time.sleep(n)
#     print('子进程:{}结束了！'.format(n))
#
#
# start_time = time.time()
# p1 = Process(target=task, args=(1,))
# p2 = Process(target=task, args=(2,))
# # p3 = Process(target=task, args=(3,))
# p3 = Process(target=task, kwargs={'n': 3})
# p1.start()
# p2.start()
# p3.start()
#
# # join()：父进程等待子进程结束
# p1.join()
# p2.join()
# p3.join()
# print('我是主进程')
# print('共耗时：{}'.format(time.time()-start_time))


''' 
或者写成下面这样的简写方式：
for循环起进程
'''

# def task(n):
#     print('这是子进程:{}'.format(n))
#     time.sleep(n)
#     print('子进程:{}结束了！'.format(n))
#
#
# start_time = time.time()
# p_list = []
# for i in range(1, 4):
#     p = Process(target=task, args=(i,))
#     # p1 = Process(target=task, kwargs={'n': i})
#     p.start()
#     p_list.append(p)
# for p in p_list:
#     p.join()
# print('我是主进程')
# print('共耗时：{}'.format(time.time() - start_time))

''' 
思考一下：
下面的代码有何不可？
这样写的问题是？ 答：这样写属于串行执行，不属于并发执行
'''

# def task(n):
#     print('这是子进程:{}'.format(n))
#     time.sleep(n)
#     print('子进程:{}结束了！'.format(n))
#
#
# start_time = time.time()
# p1 = Process(target=task, args=(1,))
# p2 = Process(target=task, args=(2,))
# p3 = Process(target=task, args=(3,))
# p1.start()
# p1.join()
# p2.start()
# p2.join()
# p3.start()
# p3.join()
#
# print('我是主进程')
# print('共耗时：{}'.format(time.time() - start_time))


''' 
通过继承Process类开启进程
除了上面这些开启进程的方法，还有一种以继承Process类的形式开启进程的方式
'''

# class MyProcess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('当前进程的pid{}'.format(os.getpid()))
#         print('%s 正在和女主播聊天' % self.name)
#
#
# p1 = MyProcess('wupeiqi')
# p2 = MyProcess('yuanhao')
# p3 = MyProcess('nezha')
#
# p1.start()  # start会自动调用run
# p2.start()
# # p2.run()
# p3.start()
#
# p1.join()
# p2.join()
# p3.join()
#
# print('主线程')


'''
守护进程
父进程中将一个子进程设置为守护进程，那么这个子进程会随着主进程的结束而结束。
主进程创建守护进程
其一：守护进程会在主进程代码执行结束后就终止
其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止
'''
''' 
守护进程的启动
'''

# class Myprocess(Process):
#     def __init__(self, person):
#         super().__init__()
#         self.person = person
#
#     def run(self):
#         print('当前进程的守护进程的pid:{}, 当前进程的pid:{}, 当前进程的守护进程的名称:{}'.format(os.getpid(), os.getppid(), self.name))
#         while 1:
#             print('{}正在和女主播聊天'.format(self.person))
#             time.sleep(1)
#
#
# p = Myprocess('二哈')
# p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
# p.start()
# print('当前进程的守护进程的pid：{}'.format(p.pid))  # 当前进程的守护进程的pid
# print('当前进程的守护进程的名称：{}'.format(p.name))  # 当前进程的守护进程的名称
# print('当前进程的pid：{}'.format(os.getpid()))  # 当前进程的pid
# print('当前进程的父进程的pid：{}'.format(os.getppid()))  # 当前进程的父进程的pid
# time.sleep(6)  # 在sleep时查看进程id对应的进程ps -ef|grep id
# print('主进程结束!')

''' 
进程代码执行结束守护进程立即结束
'''

# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
#
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
#
# p1 = Process(target=foo)
# p2 = Process(target=bar)
#
# p1.daemon = True
# p1.start()
# p2.start()
# time.sleep(0.1)
# print("main-------")  # 打印该行则主进程代码结束,则守护进程p1应该被终止.#可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.


''' 
多进程中的其他方法
'''


# class Myprocess(Process):
#     '''
#     进程对象的其他方法:terminate,is_alive
#     '''
#
#     def __init__(self, person):
#         self.name = person
#         super().__init__()
#
#     def run(self):
#         print('%s正在和网红脸聊天' % self.name)
#         print(os.getpid())
#
#
# p1 = Myprocess('哪吒')
# p1.start()
# print(os.getpid())
# print(os.getppid())
# print(p1.pid)
# # p1.terminate()  # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
# print(p1.is_alive())  # 结果为True
#
# time.sleep(3)
# print(p1.is_alive())  # 结果为False

''' 
进程对象的其他属性:pid和name
'''

class Myprocess(Process):
    def __init__(self,person):
        self.name=person   # name属性是Process中的属性，标示进程的名字
        super().__init__() # 执行父类的初始化方法会覆盖name属性
        #self.name = person # 在这里设置就可以修改进程名字了
        #self.person = person #如果不想覆盖进程名，就修改属性名称就可以了
    def run(self):
        print('%s正在和网红脸聊天' %self.name)
        # print('%s正在和网红脸聊天' %self.person)
        time.sleep(random.randrange(1,5))
        print('%s正在和网红脸聊天' %self.name)
        # print('%s正在和网红脸聊天' %self.person)

p1=Myprocess('哪吒')
p1.start()
print(p1.pid)    #可以查看子进程的进程id
