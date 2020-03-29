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
name_tuple_pattern = namedtuple('name_tuple_info', ['name', 'age', 'gender'])

my_name_tuple = name_tuple_pattern('哈哈哈', 21, gender='男')
print(my_name_tuple) # name_tuple_info(name='哈哈哈', age=21, gender='男')
print(my_name_tuple.name) # 哈哈哈
print(my_name_tuple.age) # 21
print(my_name_tuple.gender) # 男

''' 
2.字典和集合的原理和应用
2.1 散列类型的存储过程
'''



''' 
2.2 字典查找的过程
'''