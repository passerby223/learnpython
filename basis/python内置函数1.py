# coding: utf-8 
# @Time    : 2020/3/8 下午4:32
# @File    : python内置函数1.py
# @Author  : wenbin
# @Software: PyCharm


# 作⽤域相关:
# locals()：返回当前作⽤域中的名字
# globals()：返回全局作⽤域中的名字

# 迭代器相关:
# range()：⽣成数据
# next()：迭代器向下执⾏⼀次, 内部实际使⽤了__next__()⽅法返回迭代器的下⼀个项⽬
# iter()：获取迭代器, 内部实际使⽤的是__iter__()⽅法来获取迭代器

# 字符串类型代码的执⾏：
# eval()：执⾏字符串类型的代码. 并返回最终结果
# a = eval('888')
# print(a)
# print(type(a))

# exec()：执⾏字符串类型的代码
# exec('''
# number = input('请输入一个数字：')
# print('你输入的数字是{}'.format(number))
# ''')

# compile()：将字符串类型的代码变异，代码对象能够通过exec语句来执⾏或者eval()进⾏求值
'''
参数说明:
 1. resource 要执⾏的代码, 动态代码⽚段
 2. ⽂件名, 代码存放的⽂件名, 当传⼊了第⼀个参数的时候, 这个参数给空就可以了
 3. 模式, 取值有3个,
 1. exec: ⼀般放⼀些流程语句的时候
 2. eval: resource只存放⼀个求值表达式.
 3. single: resource存放的代码有交互的时候. mode应为single
'''

# code1 = "for i in range(10): print(i)"
# c1 = compile(code1, "", mode="exec")
# exec(c1)
#
# code2 = "1+2+3"
# c2 = compile(code2, "", mode="eval")
# a = eval(c2)
# print(a)
#
# code3 = "name = input('请输⼊你的名字:')"
# c3 = compile(code3, "", mode="single")
# exec(c3)
# print(name)
# 有返回值的字符串形式的代码⽤eval()，没有返回值的字符串形式的代码⽤exec()，⼀般很少⽤到compile()。

# 输入和输出相关:
# input()：获取⽤户输入的内容
# print()：打印输出

# 内存相关:
# hash()：获取到对象的哈希值(int, str, bool, tuple)
# id()：获取到对象的内存地址
# a = '12'
# print('hash', hash(a))
# print('id', id(a))

# ⽂件操作相关:
# open()：⽤于⼝打开⼀个⽂件，创建⼀个⽂件句柄

# 模块相关:
# __import__()：⽤于动态加载类和函数

# 帮助:
# help()：函数⽤于查看函数或模块⽤途的详细说明
# print(help(str))

# 调⽤相关:
# callable()：⽤于检查⼀个对象是否是可调⽤的，如果返回True，object有可能调⽤失败，但如果返回False，那调⽤绝对不会成功
# def a():
#     pass
# print(callable(a))

# 查看内置属性:
# dir()：查看对象的内置属性，⽅法，访问的是对象中的__dir__()⽅法
# a = '哈哈'
# print(a.__dir__())

# 基础数据类型相关:
# 　　数字相关: 
# bool()：将给定的数据转换成bool值，如果不给值，返回False
# int()：将给定的数据转换成int值，如果不给值, 返回0
# complex()：创建⼀个复数，第⼀个参数为实部，第⼆个参数为虚部，或者第⼀个参数直接⽤字符串来描述复数
# print(bool())# False
# print(bool(1))# True
# print(int())# 0
# print(int('4'))# 4

# 进制转换:
# bin()：将给的参数转换成⼆进制
# otc()：将给的参数转换成八进制
# hex()：将给的参数转换成⼗六进制

# 数学运算:
# abs()：返回绝对值
# divmode()：返回商和余数
# round()：四舍五入
# pow(a, b)：求a的b次幂，如果有三个参数，则求完次幂后对第三个数取余
# sum()：求和
# min()：求最⼩值
# max()：求最⼤值
# print(abs(-9))
# print(round(-9.54164, 2))
# print(pow(2, 3)) # 8
# print(pow(2, 3, 3)) # 2

''' 
和数据结构相关: 
　　列表和元组: 
list()：将⼀个可迭代对象转换成列表
tuple()：将⼀个可迭代对象转换成元组
reversed()：将⼀个序列翻转, 返回翻转序列的迭代器
slice()：列表的切片
'''
# a = range(1, 11)
# a_list = list(a)
# print(a_list)
#
# b = range(1, 11)
# b_list = tuple(b)
# print(b_list)
#
# c = reversed(a_list)
# print(reversed(a_list)) # <list_reverseiterator object at 0x7fd63240d978>
# # for i in c:
# #     print(i, end=' ')
# for i in reversed(a_list):
#     print(i, end=' ')

# print()
# a_list.reverse()
# print(a_list.reverse())# 返回None，reverse()该方法没有返回值，会对原列表的元素进行反向排序。
# print('a_list', a_list)

# index = slice(3, 10, 2)
# print(a_list[index])

# st = "⼤家好我是麻花藤"
# s = slice(1, 6, 2)
# print(st[s])

'''
字符串相关: 
str()：将数据转化成字符串
format()：与具体数据相关, ⽤于计算各种⼩数, 精算等
'''
# # 字符串
# print(format('test', '<20')) # 左对⻬
# print(format('test', '>20')) # 右对⻬
# print(format('test', '^20')) # 居中
# # 数值
# print(format(3, 'b')) # ⼆进制
# print(format(97, 'c')) # 转换成unicode字符
# print(format(11, 'd')) # ⼗进制
# print(format(11, 'o')) # ⼋进制
# print(format(11, 'x')) # ⼗六进制(⼩写字⺟)
# print(format(11, 'X')) # ⼗六进制(⼤写字⺟)
# print(format(11, 'n')) # 和d⼀样
# print(format(11)) # 和d⼀样
# # 浮点数
# print(format(123456789, 'e')) # 科学计数法. 默认保留6位⼩数
# print(format(123456789, '0.2e')) # 科学计数法. 保留2位⼩数(⼩写)
# print(format(123456789, '0.2E')) # 科学计数法. 保留2位⼩数(⼤写)
# print(format(1.23456789, 'f')) # ⼩数点计数法. 保留6位⼩数
# print(format(1.23456789, '0.2f')) # ⼩数点计数法. 保留2位⼩数
# print(format(1.23456789, '0.10f')) # ⼩数点计数法. 保留10位⼩数
# print(format(1.23456789e+10000, 'F')) # ⼩数点计数法.


# bytes()：把字符串转化成bytes类型
# s = "你好"
# bs = s.encode("UTF-8")
# print(bs)
# s1 = bs.decode("UTF-8")
# print(s1)
# bs = bytes(s, encoding="utf-8") # 把字符串编码成UTF-8
# print(bs)

# bytearray()：返回⼀个新字节数组。这个数字⾥的元素是可变的，并且每个元素的值得范围是[0,256)
# ret = bytearray('alex',encoding='utf-8')
# print(ret[0])
# print(ret)

# memoryview()：查看bytes在内存中的情况
# 查看bytes字节在内存中的情况
# s = memoryview("麻花藤".encode("utf-8"))
# print(s)

# ord()：输入字符找带字符编码的位置
# chr()：输入位置数字找出对应的字符
# ascii()：是ascii码中的返回该值 不是就返回\u...
# 找到对应字符的编码位置
# print(ord('a'))
# print(ord('中'))
# # 找到对应编码位置的字符
# print(chr(97))
# print(chr(20013))
# # 在ascii中就返回这个值. 如果不在就返回\u...
# print(ascii('a'))
# print(ascii('好'))

# repr()：返回⼀个对象的string形式
# repr 就是原封不动的输出, 引号和转义字符都不起作⽤
# print(repr('⼤家好,\n \t我叫周杰伦'))
# print('⼤家好我叫周杰伦')
#
# # %r 原封不动的写出来
# name = 'taibai'
# print('我叫%r' % name)

# 数据集合:
# dict()：创建⼀个字典
# set()：创建⼀个集合
# frozenset()：创建⼀个冻结的集合，冻结的集合不能进⾏添加和删除操作

# 　其他相关:
# len()：返回⼀个对象中的元素的个数
# sorted()：对可迭代对象进⾏排序操作(讲完lamda后再讲这个)
# enumerate()：获取集合的枚举对象

# # 可迭代对象中全部是True，结果才是True
# print(all([1, '2', True, 4.89]))
# # 可迭代对象中有⼀个是True，结果就是True
# print(any([1, None, False]))# True
# print(any([None, False]))# False


# zip()函数
# ⽤于将可迭代的对象作为参数，将对象中对应的元素打包成⼀个个元组;如果各个迭代器的元素个数不⼀致，则返回列表⻓度与最短的对象相同
list1 = [1, 2, 3]
list2 = ['1', '2', '3']
list3 = ['啦啦', '哈哈', '呵呵', '噢噢']
for i in zip(list1, list2, list3):
    print(i)
''' 
(1, '1', '啦啦')
(2, '2', '哈哈')
(3, '3', '呵呵')
'''

# fifilter()：过滤(讲完lamda)
# map()：会根据提供的函数对指定序列做映射(lamda)

