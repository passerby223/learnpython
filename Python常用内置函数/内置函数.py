# @Time    : 2020/4/3 上午12:38
# @File    : 内置函数.py
# @Author  : _anonymous
# @Software: PyCharm
import os

'''
filter函数 用于过滤序列
'''

# def func(n):
#     return n > 5


# list1 = [1, 2, 32, 4, 3, 5, 4, 5665, 766, 8, 32]

# res = filter(func, list1)  # 对数据做过滤，传入一个list，会依次从list中取出每个元素当做func函数的入参n，然后将满足func函数的返回值保存起来
# print(res)  # <filter object at 0x7f3f34bffba8>
# print(list(res))  # [32, 5665, 766, 8, 32] 将list1中大于5的数筛选出来，再通过list方法装换成list形式

''' 
map函数 会根据提供的函数对指定序列做映射
'''
# res1 = map(func, list1)
# print(res1)  # <map object at 0x7f0483c3afd0>
# 将list1中大于5的数筛选出来，再通过list方法装换成list形式,list中保存的是满足n>5的为True，否则为False
# print(list(res1))  # [False, False, True, False, False, False, False, True, True, True, True]

''' 
zip函数 用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
'''

# res2 = zip(['name', 'age', 'hobby'], ['潇潇', '21', 'programing'])
# dict1 = {'name': '潇潇', 'age': '21', 'hobby': 'programing'}
# print(res2)  # <zip object at 0x7f0cb0387288>
# print(list(res2)) # [('name', '潇潇'), ('age', '21'), ('hobby', 'programing')]
# print(dict(list(res2))) #
# print(list(dict1.items())) # [('name', '潇潇'), ('age', '21'), ('hobby', 'programing')]

'''
匿名函数
lambda
用途：节省内存和美观
使用场景：经常搭配filter()函数和map()函数使用,也可以配合推导式进行使用，还可以配合三目运算符使用
'''
# 配合filter()函数和map()函数使用
list1 = [1, 2, 32, 4, 3, 5, 4, 5665, 766, 8, 32]
res = filter(lambda n: n > 5, list1)
res1 = map(lambda n: n > 5, list1)
print(list(res))  # [32, 5665, 766, 8, 32]
print(list(res1))  # [False, False, True, False, False, False, False, True, True, True, True]

''' 
lambda配合推导式使用,很少这样用
'''
res2 = [(lambda n: n > 5)(i) for i in range(1, 11)]
print(res2)  # [False, False, False, False, False, True, True, True, True, True]

''' 
Python中的三目运算符
'''
# 普通写法
a = 4
if a > 3:
    print('a > 3')  # a > 3
else:
    print('a < 3')
# 三目运算符写法
print('a > 3') if a > 3 else print('a < 3')  # a > 3

''' 
Python中的偏函数 partial
减少地代码复用
'''
list2 = [1, 2, 32, 4, 3, 5, 4, 5665, 766, 8, 32]
list3 = [13, 13, 16, 1651, 61, 6, 16, 1456, 4156]
list4 = [46, 84, 894, 89, 489, 49, 4, ]
from functools import partial

filter_customize = partial(filter, lambda n: n > 200)  # filter:过滤函数
res3 = filter_customize(list2)
res4 = filter_customize(list3)
res5 = filter_customize(list4)
print('res3>>>', list(res3))  # res3>>> [5665, 766]
print('res4>>>', list(res4))  # res4>>> [1651, 1456, 4156]
print('res5>>>', list(res5))  # res5>>> [894, 489]
