# coding: utf-8 
# @Time    : 2020/3/25 上午12:14
# @File    : gevent_test.py
# @Author  : Always be conding
# @Software: PyCharm


'''
协程gevent
'''
# import gevent
#
#
# def eat(name):
#     print('%s eat 1' % name)
#     gevent.sleep(2)
#     print('%s eat 2' % name)
#
#
# def play(name):
#     print('%s play 1' % name)
#     gevent.sleep(1)
#     print('%s play 2' % name)
#
#
# g1 = gevent.spawn(eat, 'egon')
# g2 = gevent.spawn(play, name='egon')
# # g1.join()
# # g2.join()
# # 或者
# gevent.joinall([g1, g2])
# print('主')

''' 
上例gevent.sleep(2)模拟的是gevent可以识别的io阻塞,而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了。

from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面，如time，socket模块之前。

或者我们干脆记忆成：要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头。
'''
# from gevent import monkey
#
# monkey.patch_all()
# import gevent
# import time
#
#
# def eat():
#     print('eat food 1')
#     time.sleep(2)
#     print('eat food 2')
#
#
# def play():
#     print('play 1')
#     time.sleep(1)
#     print('play 2')
#
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# gevent.joinall([g1, g2])
# print('主')

''' 
我们可以用threading.current_thread().getName()来查看每个g1和g2，查看的结果为DummyThread-n，即假线程。

查看threading.current_thread().getName()：
'''
# from gevent import monkey;
#
# monkey.patch_all()
# import threading
# import gevent
# import time
#
#
# def eat():
#     print(threading.current_thread().getName())
#     print('eat food 1')
#     time.sleep(2)
#     print('eat food 2')
#
#
# def play():
#     print(threading.current_thread().getName())
#     print('play 1')
#     time.sleep(1)
#     print('play 2')
#
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# gevent.joinall([g1, g2])
# print('主')

''' 
Gevent的同步和异步
'''
# from gevent import spawn, joinall, monkey
#
# monkey.patch_all()
# import time
#
#
# def task(pid):
#     """
#     Some non-deterministic task
#     """
#     time.sleep(0.5)
#     print('Task %s done' % pid)
#
#
# def synchronous():  # 同步
#     for i in range(10):
#         task(i)
#
#
# def asynchronous():  # 异步
#     g_l = [spawn(task, i) for i in range(10)]
#     joinall(g_l)
#     print('DONE')
#
#
# if __name__ == '__main__':
#     print('Synchronous:')
#     synchronous()
#     print('Asynchronous:')
#     asynchronous()
#  上面程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。
#  初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 函数，
#  后者阻塞当前流程，并执行所有给定的greenlet任务。执行流程只会在 所有greenlet执行完后才会继续向下走。
