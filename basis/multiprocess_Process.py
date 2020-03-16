# coding: utf-8 
# @Author  : wenbin
# @Time    : 2020/3/16 上午11:04
# @Software: PyCharm
# @File    : multiprocess_Process.py


from multiprocessing import Process

import time


def task(name, msg):
    print('{}{}'.format(name, msg))
    print('{} is running!'.format(name))
    time.sleep(2)
    print('{} is done!'.format(name))


# 以位置参数进行传参，位置参数需要放到一个元组中
p = Process(target=task, args=('task1', '进程已成功启动!'))
# 以关键字参数进行传参，关键字参数需要放到一个字典dict中
p1 = Process(target=task, kwargs={'name': 'task2', 'msg': '进程已成功启动!'})
# 以关键字参数进行传参时，如果形参与task方法中的形参变量名不一致会报错：TypeError: task() got an unexpected keyword argument 'name1'
# p2 = Process(target=task, kwargs={'name1': 'task3', 'msg': '进程已成功启动!'})
p.start() # 启动进程
p1.start() # 启动进程
# p2.start() # 启动进程
print(p.pid) # 打印进程4的PID
print(p1.pid) # 打印进程的PID
# print(p2.pid) # 打印进程的PID
time.sleep(10) # 休眠以便使用'ps -elf | grep PID  | grep -v grep'可以查看到该进程
print('程序结束'.center(10, '-'))

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