# coding: utf-8 
# @Author  : wenbin
# @Time    : 2020/3/12 下午12:52
# @Software: PyCharm
# @File    : isinstance_issubclass.py


# '''
# 1.1 isinstance
# isinstance(obj,cls)检查是否obj是否是类 cls 的对象
# '''
# a = 's'
# print(isinstance(a, str))
#
#
# class Foo(object):
#     pass
#
#
# obj = Foo()
#
# print(isinstance(obj, Foo))
# '''
# 例子
# '''
# print('分割线'.center(50, '*'))
# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# obj1 = Foo()
# print(isinstance(obj1, Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
# print(isinstance(obj1, Base))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
# print('分割线'.center(50, '*'))
# obj2 = Base()
# print(isinstance(obj2, Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
# print(isinstance(obj2, Base))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
#
# '''
# issubclass
# issubclass(sub, super)检查sub类是否是 super 类的派生类
# '''
# print('分割线'.center(50, '*'))
#
#
# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# class Bar(Foo):
#     pass
#
#
# print(issubclass(Bar, Base))  # 检查第一个参数是否是第二个参数的 子子孙孙类
# '''
# type
# 获取当前对象是由哪个类创建。
# '''
# a1 = Bar()
# print(type(a1)) # <class '__main__.Bar'>
# if type(a1) == Bar:
#     print('1')

'''
例子
'''
# print('分割线'.center(50, '*'))
#
#
# class Foo(object):
#     pass
#
#
# class Bar(object):
#     pass
#
#
# def func(*args):
#     foo_counter = 0
#     bar_counter = 0
#     for item in args:
#         if type(item) == Foo:
#             foo_counter += 1
#         elif type(item) == Bar:
#             bar_counter += 1
#     return foo_counter, bar_counter
#
#
# result = func(Foo(),Bar(),Foo())
# print(result)
# v1, v2 = func(Foo(), Bar(), Foo())
# print(v1, v2)

'''
反射
3.1 什么是反射
反射的概念是由Smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力（自省）。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用,并在Lisp和面向对象方面取得了成绩。 
3.2 python中的反射
python面向对象中的反射：通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）。
四个可以实现自省的函数：
hasattr()
getattr()
setattr()
delattr()
'''

# hasattr()
# getattr()
# setattr()
# delattr()

class Foo:
    f = '类的静态变量'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('hi,%s' % self.name)


obj = Foo('egon', 23)
# 检测是否含有某属性
print(hasattr(obj, 'name'))
print(hasattr(obj, 'say_hi'))
print('分割线'.center(50, '*'))
# 获取属性
n = getattr(obj, 'name')
print(n)
func = getattr(obj, 'say_hi')
func()
# print(getattr(obj, 'aaaaaaaa'))  # 报错:AttributeError: 'Foo' object has no attribute 'aaaaaaaa'
print(getattr(obj, 'aaaaaaaa', '默认值'))  # 可以手动设置一个默认值哦：When a default argument is given, it is returned when the attribute doesn't exist; without it, an exception is raised in that case.

print('分割线'.center(50, '*'))
# 设置属性
setattr(obj, 'sb', True)
setattr(obj, 'show_name', lambda self: self.name + 'is a sb')
print(obj.__dict__)
print(obj.show_name(obj))
print('分割线'.center(50, '*'))
# 删除属性
delattr(obj, 'age')
delattr(obj, 'show_name')
# delattr(obj, 'show_name111')  # 不存在,则报错：AttributeError: show_name111

print(obj.__dict__)

print('分割线'.center(50, '*'))
import sys
print(sys.modules.get('_io')) # <module 'io' (built-in)>
print(sys.modules[__name__])

# 导入其他模块，利用反射查找该模块是否存在某个方法。
print('分割线'.center(50, '*'))
from basis import module_test as mt
hasattr(mt, '_1test')
print(hasattr(mt, '_1test'))
getattr(mt, '_1test')() # from the test
print(getattr(mt, '_1test1', '哈哈'))