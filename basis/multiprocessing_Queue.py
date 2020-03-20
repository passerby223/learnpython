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

