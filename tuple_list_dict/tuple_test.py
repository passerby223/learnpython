'''
-*- coding: utf-8 -*-
@Author  : ABC
@Time    : 2019/10/16 23:42
@Software: PyCharm
@File    : tuple_test.py
'''
tuple1 = ('哈哈', 2, 45)
tuple2 = tuple1 + ('啦啦',) + ('th',) * 5
print(tuple2)
a = 9
print(str(a) + tuple2[a-1])
