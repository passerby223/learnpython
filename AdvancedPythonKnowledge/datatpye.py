# @Time    : 2020/3/28 下午11:27
# @File    : datatype.py
# @Author  : Always be codding
# @Software: PyCharm
import timeit
from collections import namedtuple

"""
1.元组和列表
1.1 元组和列表性能比较分析
1.2 命名元组
2.字典和集合的原理和应用
2.1 散列类型的存储过程
2.2 字典查找的过程

3.推导式
3.1 列表推导式
3.2 字典推导式
3.3 生成器表达式

4.迭代器和生成器
4.1 生成器
4.2 迭代协议
4.3 迭代器
"""

''' 
1.1 元组和列表性能比较分析
'''

# def func():
#     for i in range(1, 4):
#         pass
#
#
# res1 = timeit.timeit('(1, 2, 3)')
# print('元组执行10000000次消耗{}秒'.format(res1))
# res = timeit.timeit('[1, 2, 3]')
# print('列表执行10000000次消耗{}秒'.format(res))
# res2 = timeit.timeit(func)
# print('方法执行10000000次消耗{}秒'.format(res2))

'''
1.2 命名元组 规则
'''
# name_tuple_pattern = namedtuple('name_tuple_info', ['name', 'age', 'gender'])
#
# my_name_tuple = name_tuple_pattern('哈哈哈', 21, gender='男')
# print(my_name_tuple)  # name_tuple_info(name='哈哈哈', age=21, gender='男')
# print(my_name_tuple.name)  # 哈哈哈
# print(my_name_tuple.age)  # 21
# print(my_name_tuple.gender)  # 男
'''
1.3 集合和字典
'''
# set1 = set()
# set2 = {1, 2, 3, 4, '哈哈'}
# dict1 = {"name": "张三", "age": 21}
# print(type(set1), type(set2), type(dict1)) # <class 'set'> <class 'set'> <class 'dict'>
# print(set1, set2, dict1) # set() {1, 2, 3, 4, '哈哈'} {'name': '张三', 'age': 21}
''' 
集合的方法
集合set是无序的，可以用来去重
'''
# set1.add('hello1')
# set1.add('hello2')
# set1.add('hello3')
# print(set1)
# set1.remove("hello1")
# print(set1)
# set1.add('hello4')
# set1.add('hello5')
# set1.pop() # 随机删除集合中的一个元素
# print(set1)
# set1.clear() # 清空集合中的所有元素
# print(set1) #　set()
# # 使用update(等同于list的extend方法)一次性向集合中添加多个元素
# set1.update(['111', "222", '333', '叭叭叭'])
# print(set1)
# set1.update(('444', "555", '666', '喇喇喇'))
# print(set1)
# set1.update({'777', "888", '999', '噜噜啦'})
# print(set1)

''' 
利用set集合中元素唯一的特性对list进行去重
'''
# list1 = [111, 111, 65, 89, 78, 89, 65, 78, "啦啦啦"]
# list1_new = list(set(list1))
# print("list1>>>{}, list1_new>>>{}".format(list1, list1_new))

''' 
2.字典和集合的原理和应用
2.1 散列类型的存储过程
2.2 字典查找的过程
Python中数据类型分类：
数值：1
序列类型：list,tuple
散列类型：dict,set

Python中数据类型可分为：可变类型和不可变类型(可hash的)

性能分析
查找元素时间：集合>字典>元组>列表
占用内存比较：字典>集合>列表>元组
'''

''' 
列表推导式
'''
# list_sheep = ['{}只羊'.format(i) for i in range(1, 11)]
# print('一共生成了{}只羊>>>{}'.format(len(list_sheep), list_sheep))

'''
字典推导式
'''
# dict_sheep = {str(i): '第{}只羊'.format(str(i)) for i in range(1, 11)}
# print('一共生成了{}只羊>>>{}'.format(len(dict_sheep), dict_sheep))

'''
小练习
将下边的字符串改成字典形式
'''
# cookie = 'UM_distinctid1=16f0634db1070;UM_distinctid2=066d9e63a3bcb4;UM_distinctid3=31760856;UM_distinctid4=1fa400'
# cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookie.split(';')}
# print(cookie_dict)

''' 
生成器表达式
'''
# 如果最外层用`[]`的话，此表达式就是一个列表推导式
# 如果最外层用`{}`的话，此表达式就是一个字典推导式
# 如果最外层用`()`的话，会产生成一个生成器对象，次表达式称为生成器表达式
'''
思考
为什么要使用生成器？
定义一个生成器对象，不会占用很大的内存，它只是定义了一个生成器规则
不会像列表推导式、字典推导式那样直接生成一个list、dict存放在内存中，这样会很占用内存。
'''
# generator = (i for i in range(1, 11))
# print(generator)  # 生成器对象：<generator object <genexpr> at 0x7f6b2e033360>
# print(next(generator))  # 生成器对象的值可以通过next()方法依次取值
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())  # 报错：StopIteration 停止迭代

''' 
yield 关键字的使用，yield关键字只能在函数中中使用

'''


