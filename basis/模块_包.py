# coding: utf-8 
# @Time    : 2020/3/11 下午10:33
# @File    : 模块_包.py
# @Author  : wenbin
# @Software: PyCharm

import json
''' 
1. 模块
1.1 什么是模块
别人写好的函数、变量、方法放在一个文件里 (这个文件可以被我们直接使用)这个文件就是个模块

常见的场景：一个模块就是一个包含了python定义和声明的文件，文件名就是模块名字加上.py的后缀。

但其实import加载的模块分为四个通用类别：

1.使用python编写的代码（.py文件）

2.已被编译为共享库或DLL的C或C++扩展

3.包好一组模块的包

4.使用C编写并链接到python解释器的内置模块

1.2 为什么要使用模块
如果你退出python解释器然后重新进入，那么你之前定义的函数或者变量都将丢失，因此我们通常将程序写到文件中以便永久保存下来，需要时就通过python test.py方式去执行，此时test.py被称为脚本script。

随着程序的发展，功能越来越多，为了方便管理，我们通常将程序分成一个个的文件，这样做程序的结构更清晰，方便管理。这时我们不仅仅可以把这些文件当做脚本去执行，还可以把他们当做模块来导入到其他的模块中，实现了功能的重复利用。

1.3 如何使用模块
1.3.1 import
示例文件：自定义模块my_module.py
'''
# # my_module.py
# print('from the my_module.py')
# money = 1000
#
#
# def read1():
#     print('my_module->read1->money', money)
#
#
# def read2():
#     print('my_module->read2 calling read1')
#     read1()
#
#
# def change():
#     global money
#     money = 0

''' 
模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，它们只在模块名第一次遇到导入import语句时才执行（import语句是可以在程序中的任意位置使用的，且针对同一个模块很import多次，为了防止你重复导入。
python的优化手段是：第一次导入后就将模块名加载到内存了，后续的import语句仅是对已经加载大内存中的模块对象增加了一次引用，不会重新执行模块内的语句），如下 ：
'''
from basis import random_time_sys_os
print('a')
# import basis.random_time_sys_os
# import basis.random_time_sys_os