# coding: utf-8 
# @Time    : 2020/3/18 下午9:32
# @File    : multiprocessing_Queue.py
# @Author  : wenbin
# @Software: PyCharm


import time
import threading
from threading import Thread
from multiprocessing import Process

'''
单看队列用法
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

# from multiprocessing import Queue
# import queue
# q1 = queue.Queue()
# q=Queue(3)
#
# #put ,get ,put_nowait,get_nowait,full,empty
# q.put(3)
# q.put(3)
# q.put(3)
# # q.put(3)   # 如果队列已经满了，程序就会停在这里，等待数据被别人取走，再将数据放入队列。
#            # 如果队列中的数据一直不被取走，程序就会永远停在这里。
# try:
#     q.put_nowait(3) # 可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
# except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去，但是会丢掉这个消息。
#     print('队列已经满了')
#
# # 因此，我们再放入数据之前，可以先看一下队列的状态，如果已经满了，就不继续put了。
# print(q.full()) #满了
#
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q.get()) # 同put方法一样，如果队列已经空了，那么继续取就会出现阻塞。
# try:
#     q.get_nowait(3) # 可以使用get_nowait，如果队列满了不会阻塞，但是会因为没取到值而报错。
# except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去。
#     print('队列已经空了')
#
# print(q.empty()) #空了
import os

''' 
上面这个例子还没有加入进程通信，只是先来看看队列为我们提供的方法，以及这些方法的使用和现象。
子进程发送数据给父进程
'''
# import time
# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([time.strftime('%Y-%m-%d %H:%M:%S'), 'hi', 'hello'])  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。
#     q.put([time.asctime(), 'hi', 'hello'])  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。
#
# q = Queue() #创建一个Queue对象
# p = Process(target=f, args=(q,)) #创建一个进程
# p.start()
# print('q.get()：{}'.format(q.get()))
# print('q.get()：{}'.format(q.get()))
# p.join()


''' 
上面是一个queue的简单应用，使用队列q对象调用get函数来取得队列中最先进入的数据。 接下来看一个稍微复杂一些的例子：
批量生产数据放入队列再批量获取结果 x
'''
# import os
# import time
# import multiprocessing
#
# # 向queue中输入数据的函数
# def inputQ(queue):
#     info = str(os.getpid()) + '(put):' + str(time.asctime())
#     queue.put(info)
#
# # 向queue中输出数据的函数
# def outputQ(queue):
#     info = queue.get()
#     print ('%s%s\033[32m%s\033[0m'%(str(os.getpid()), '(get):',info))
#
# # Main
# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     record1 = []   # store input processes
#     record2 = []   # store output processes
#     queue = multiprocessing.Queue(3)
#
#     # 输入进程
#     for i in range(10):
#         process = multiprocessing.Process(target=inputQ,args=(queue,))
#         process.start()
#         record1.append(process)
#
#     # 输出进程
#     for i in range(10):
#         process = multiprocessing.Process(target=outputQ,args=(queue,))
#         process.start()
#         record2.append(process)
#
#     for p in record1:
#         p.join()
#
#     for p in record2:
#         p.join()

''' 
生产者消费者模型
在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产数据和消费数据的工作能力来提高程序的整体处理数据的速度。
为什么要使用生产者和消费者模式
生产者就是生产数据的一方，消费者就是消费数据的一方。通常生产者和消费者的能力很难协调，例如：如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。
什么是生产者消费者模式
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。
基于队列实现生产者消费者模型:
'''
# from multiprocessing import Process, Queue
# import time, random, os
#
#
# def consumer(q):
#     '''
#     消费者
#     :param q:
#     :return:
#     '''
#     while True:
#         res = q.get()
#         time.sleep(random.randint(1, 3))
#         print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))
#
#
# def producer(q):
#     '''
#     生产者
#     :param q:
#     :return:
#     '''
#     for i in range(10):
#         time.sleep(random.randint(1, 3))
#         res = '包子%s' % i
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=(q,))
#
#     # 消费者们:即吃货们
#     c1 = Process(target=consumer, args=(q,))
#
#     # 开始
#     p1.start()
#     c1.start()
#     print('主')

''' 
此时的问题是主进程永远不会结束，原因是：生产者p在生产完后就结束了，但是消费者c在取空了q之后，则一直处于死循环中且卡在q.get()这一步。
解决方式无非是让生产者在生产完毕后，往队列中再发一个结束信号，这样消费者在接收到结束信号后就可以break出死循环。
 改良版——生产者消费者模型:
'''

# from multiprocessing import Process, Queue
# import time, random, os
#
#
# def consumer(q):
#     while True:
#         res = q.get()
#         if res is None: break  # 收到结束信号则结束
#         time.sleep(random.randint(1, 3))
#         print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))
#
#
# def producer(q):
#     for i in range(10):
#         time.sleep(random.randint(1, 3))
#         res = '包子%s' % i
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
#     q.put(None)  # 发送结束信号
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=(q,))
#
#     # 消费者们:即吃货们
#     c1 = Process(target=consumer, args=(q,))
#
#     # 开始
#     p1.start()
#     c1.start()
#     print('主')


''' 
注意：结束信号None，不一定要由生产者发，主进程里同样可以发，但主进程需要等生产者结束后才应该发送该信号
主进程在生产者生产完毕后发送结束信号None:
'''
# from multiprocessing import Process,Queue
# import time,random,os
# def consumer(q):
#     while True:
#         res=q.get()
#         if res is None:break #收到结束信号则结束
#         time.sleep(random.randint(1,3))
#         print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))
#
# def producer(q):
#     for i in range(2):
#         time.sleep(random.randint(1,3))
#         res='包子%s' %i
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,))
#
#     #开始
#     p1.start()
#     c1.start()
#
#     p1.join()
#     q.put(None) #发送结束信号
#     print('主')

''' 
多个消费者的例子：有几个消费者就需要发送几次结束信号
'''
# from multiprocessing import Process, Queue
# import time, random, os
#
#
# def consumer(q):
#     while True:
#         res = q.get()
#         if res is None: break  # 收到结束信号则结束
#         time.sleep(random.randint(1, 3))
#         print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))
#
#
# def producer(name, q):
#     for i in range(2):
#         time.sleep(random.randint(1, 3))
#         res = '%s%s' % (name, i)
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=('包子', q))
#     p2 = Process(target=producer, args=('骨头', q))
#     p3 = Process(target=producer, args=('泔水', q))
#
#     # 消费者们:即吃货们
#     c1 = Process(target=consumer, args=(q,))
#     c2 = Process(target=consumer, args=(q,))
#
#     # 开始
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#
#     p1.join()  # 必须保证生产者全部生产完毕,才应该发送结束信号
#     p2.join()
#     p3.join()
#     q.put(None)  # 有几个消费者就应该发送几次结束信号None
#     q.put(None)  # 发送结束信号
#     print('主')


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
from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


t = Thread(target=sayhi, args=('egon',))
t.start()
t.join()
print('主线程')
print(t.is_alive())
'''
egon say hello
主线程
False
'''
