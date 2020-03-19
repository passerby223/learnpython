# coding: utf-8 
# @Author  : wenbin
# @Time    : 2020/3/18 上午10:57
# @Software: PyCharm
# @File    : queue_test.py


import queue
import time

'''
方法介绍
Queue([maxsize])
创建共享的进程队列。maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。底层队列使用管道和锁定实现。
另外，还需要运行支持线程以便队列中的数据传输到底层管道中。
Queue的实例q具有以下方法：
q.get( [ block [ ,timeout ] ] )
返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行为，默认为True. 如果设置为False，
将引发Queue.Empty异常（定义在Queue模块中）。
timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。
q.get_nowait( )
同q.get(False)方法。
q.put(item [, block [,timeout ] ] )
将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。block控制阻塞行为，默认为True。如果设置为False，
将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短。超时后将引发Queue.Full异常。
q.qsize()
返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。
在某些系统上，此方法可能引发NotImplementedError异常。
q.empty()
如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。
也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。
q.full()
如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的（参考q.empty（）方法）。。
'''
# my_queue = queue.Queue(maxsize=199) # maxsize是设置队列的长度，会报queue.Full异常
# my_queue = queue.Queue(maxsize=200) # maxsize是设置队列的长度，会报queue.Full异常
my_queue = queue.Queue(maxsize=201)  # maxsize是设置队列的长度，会报queue.Full异常
# my_queue = queue.Queue() # 如果不填,maxsize=0，也就是队列长度无大小限制

# with open('queue_data', mode='a+', encoding='utf-8') as file:
# for i in range(1, 201):
#     file.write('data' + str(i) + '\n')

with open('queue_data', mode='r', encoding='utf-8') as file:
    count = 0
    for i in file:
        count += 1
        print('当前队列是否为空：{}'.format(my_queue.empty()))  # 第一次运行时：当前队列是否为空：True
        my_queue.put(i.strip('\n'))
        print('当前队列中的长度：{}'.format(my_queue.qsize()))
        print('my_queue.full:{}, count计数器:{}'.format(my_queue.full(), count))  # my_queue.full:False, count计数器:200
        # my_queue.put(i.strip('\n'), block=False)
        # print('my_queue.full:{}, count计数器:{}'.format(my_queue.full(), count)) # my_queue.full:True, count计数器:199
        # my_queue.put_nowait(i.strip('\n')) # put_nowait(i.strip('\n'))等同于put(i.strip('\n'), block=False)
        # print('my_queue.full:{}, count计数器:{}'.format(my_queue.full(), count)) # my_queue.full:True, count计数器:199

while 1:
    '''
    get_nowait()等同于get(block=False)
    '''
    # data = my_queue.get(block=False) # 当队列中的数据消费完之后，会抛出queue.Empty异常
    # data = my_queue.get_nowait() # 当队列中的数据消费完之后，会抛出queue.Empty异常
    # data = my_queue.get(timeout=5)
    data = my_queue.get()
    # my_queue.put(data) # 消费一个data后再将data放回my_queue中
    print(data)


# 其他方法(了解)
# q.close()
# 关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，但将在此方法完成时马上关闭。如果q被垃圾收集，将自动调用此方法。关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。例如，如果某个使用者正被阻塞在get（）操作上，关闭生产者中的队列不会导致get（）方法返回错误。
# q.cancel_join_thread()
# 不会再进程退出时自动连接后台线程。这可以防止join_thread()方法阻塞。
# q.join_thread()
# 连接队列的后台线程。此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为。


