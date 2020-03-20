# coding: utf-8 
# @Time    : 2020/3/20 下午11:33
# @File    : threading_test.py
# @Author  : Always be conding
# @Software: PyCharm


'''
线程
线程介绍
有了进程为什么要有线程
进程有很多优点，它提供了多道编程，让我们感觉我们每个人都拥有自己的CPU和其他资源，可以提高计算机的利用率。
很多人就不理解了，既然进程这么优秀，为什么还要线程呢？其实，仔细观察就会发现进程还是有很多缺陷的，主要体现在两点上：

进程只能在一个时间干一件事，如果想同时干两件事或多件事，进程就无能为力了。

进程在执行的过程中如果阻塞，例如等待输入，整个进程就会挂起，即使进程中有些工作不依赖于输入的数据，也将无法执行。

如果这两个缺点理解比较困难的话，举个现实的例子也许你就清楚了：如果把我们上课的过程看成一个进程的话，那么我们要做的是耳朵听老师讲课，
手上还要记笔记，脑子还要思考问题，这样才能高效的完成听课的任务。而如果只提供进程这个机制的话，上面这三件事将不能同时执行，同一时间只能做一件事
，听的时候就不能记笔记，也不能用脑子思考，这是其一；如果老师在黑板上写演算过程，我们开始记笔记，而老师突然有一步推不下去了，
阻塞住了，他在那边思考着，而我们呢，也不能干其他事，即使你想趁此时思考一下刚才没听懂的一个问题都不行，这是其二。

现在你应该明白了进程的缺陷了，而解决的办法很简单，我们完全可以让听、写、思三个独立的过程，并行起来，这样很明显可以提高听课的效率。
而实际的操作系统中，也同样引入了这种类似的机制——线程。

线程的出现
60年代，在OS中能拥有资源和独立运行的基本单位是进程，然而随着计算机技术的发展，进程出现了很多弊端，一是由于进程是资源拥有者，
创建、撤消与切换存在较大的时空开销，因此需要引入 轻型进程 ；二是由于对称多处理机（SMP）出现， 可以满足多个运行单位 ，而多个进程并行开销过大。
因此在80年代，出现了 能独立运行的基本单位 ——线程（Threads） 。
注意：进程是资源分配的最小单位,线程是CPU调度的最小单位.
每一个进程中至少有一个线程。
进程和线程的关系
'''
'''
Python中使用线程一
'''

# def task(name):
#     time.sleep(3)
#     print('hello {}!'.format(name))
#
#
# t1 = Thread(target=task, args=('Jack',))
# t1.start()
# t1.join()  # 等待线程终止
# print('主线程结束!')

'''
Python中使用线程二
继承Thread类
'''

# class MyThread(Thread):
#
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         time.sleep(2)
#         print('hello {}!'.format(self.name))
#
#
# t1 = MyThread(name='啦啦啦')
# t1.start()
# t1.join()
# print('主线程结束!')

'''
多线程与多进程
'''

# def task():
#     print('hello {}'.format(os.getpid()))
#
#
# # 多进程
#
# # part1:开多个进程,每个进程都有不同的pid
# p1 = Process(target=task)  # hello 16562
# p2 = Process(target=task)  # hello 16563
# p3 = Process(target=task)  # hello 16564
# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()
# print('主线程/主进程pid', os.getpid()) # 主线程/主进程pid 16561
#
# time.sleep(3)
# # 多线程
#
# # part2:在主进程下开启多个线程,每个线程都跟主进程的pid一样
# t1 = Thread(target=task)  # hello 16561
# t2 = Thread(target=task)  # hello 16561
# t3 = Thread(target=task)  # hello 16561
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print('主线程/主进程pid', os.getpid()) # 主线程/主进程pid 16561

'''
线程与进程开启效率的较量
'''

# def work():
#     print('hello')
#
#
# if __name__ == '__main__':
#     # 在主进程下开启线程
#     t = Thread(target=work)
#     t.start()
#     print('主线程/主进程')
#     '''
#     打印结果:
#     hello
#     主线程/主进程
#     '''
#     print('分割线'.center(50, '*'))
#     # 在主进程下开启子进程
#     t = Process(target=work)
#     t.start()
#     print('主线程/主进程')
#     '''
#     打印结果:
#     主线程/主进程
#     hello
#     '''


'''
同一进程内的线程共享该进程的数据？
内存数据的共享问题
'''

# def work():
#     global n
#     n = 0
#     print('子', n)


# n = 100
# p = Process(target=work)
# p.start() # 子 0
# p.join()
# print('主', n)  # 主 100 , 毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100

# print('分割线'.center(50, '*'))
#
# n = 1
# t = Thread(target=work)
# t.start()  # 子 0
# t.join()
# print('主', n)  # 主 0 , 查看结果为0,因为同一进程内的线程之间共享进程内的数据


'''
Thread类的其他方法 
Thread实例对象的方法
  # isAlive(): 返回线程是否活动的。
  # getName(): 返回线程名。
  # setName(): 设置线程名。

threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程变量。
  # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
  # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
'''

'''
代码示例1
'''
# from threading import Thread
# import threading
# from multiprocessing import Process
# import os
#
#
# def work():
#     time.sleep(3)
#     print(threading.current_thread().getName())
#
#
# # 在主进程下开启线程
# t = Thread(target=work)
# t.start()
#
# print(threading.current_thread().getName())
# print(threading.current_thread())  # 主线程
# print(threading.enumerate())  # 连同主线程在内有两个运行的线程
# print(threading.active_count())
# print('主线程/主进程')

'''
打印结果:
MainThread
<_MainThread(MainThread, started 140735268892672)>
[<_MainThread(MainThread, started 140735268892672)>, <Thread(Thread-1, started 123145307557888)>]
主线程/主进程
Thread-1
'''

'''
代码示例2
'''
# def task():
#     time.sleep(3)
#     print('PID:{}'.format(os.getpid()))
#
#
# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)
# t3 = threading.Thread(target=task)
# start_time = time.time()
# t1.start()
# t2.start()
# t3.start()
# print('threading.currentThread():{}'.format(threading.currentThread()))
# print('threading.enumerate(): {}'.format(threading.enumerate()))
# print('threading.activeCount(): :{}'.format(threading.activeCount()))
# print('t1线程名：{}'.format(t1.name))
# print('t2线程未重命名前：{}'.format(t2.getName()))
# t2.setName('我是线程2')
# print('t2线程重命名后：{}'.format(t2.getName()))
# print('t3线程名：{}'.format(t3.name))
# print(t1.isAlive())  # True Return whether the thread is alive
# print(t2.is_alive())  # True Return whether the thread is alive
# print(t3.is_alive())  # True Return whether the thread is alive
# time.sleep(5)
# print(t1.isAlive())  # False Return whether the thread is alive
# print(t2.is_alive())  # False Return whether the thread is alive
# print(t3.is_alive())  # False Return whether the thread is alive
# end_time = time.time()
# spend_time = end_time - start_time


# print('从所有线程启动到程序结束总共花费{}s'.format(spend_time))  # 从所有线程启动到程序结束总共花费5.002387285232544s 只可以是接近5秒，因为启动线程包括打印输出也需要花费时间。进一步说明了线程是并发执行的。


'''
join()方法
代码示例
'''
# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# t = Thread(target=sayhi, args=('egon',))
# t.start()
# t.join()
# print('主线程')
# print(t.is_alive())
'''
egon say hello
主线程
False
'''

'''
守护线程
无论是进程还是线程，都遵循：守护xx会等待主xx运行完毕后被销毁。 需要强调的是：运行完毕并非终止运行

#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕

#1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，
#2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。
'''
''' 
 守护线程例1
'''
# from threading import Thread
# import time
#
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# t = Thread(target=sayhi, args=('egon',))
# t.setDaemon(True)  # 必须在t.start()之前设置
# t.start()
#
# print('主线程')
# print(t.is_alive())

''' 
 守护线程例2
'''
from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.daemon = True
t1.start()
t2.start()
print("main-------")
