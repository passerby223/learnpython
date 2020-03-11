# coding: utf-8 
# @Time    : 2020/3/11 下午10:09
# @File    : 异常和错误.py
# @Author  : wenbin
# @Software: PyCharm

'''
异常和错误
1.1 错误
程序中难免出现错误，而错误分成两种
1.1.1 语法错误
语法错误：这种错误，根本过不了python解释器的语法检测，必须在程序执行前就改正。
SyntaxError: invalid syntax
'''
# # 语法错误示范一
# if
#
# # 语法错误示范二
# def test:
#     pass
# # 语法错误示范三
# print(haha
''' 
逻辑错误
'''
# 用户输入不完整(比如输入为空)或者输入非法(输入不是数字)
# ValueError
# num = input(">>: ")
# int(num)
# # 无法完成计算
# res1 = 1 / 0
# res2 = 1 + 'str'

''' 
python中常用异常
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类）；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
更多异常
ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
'''

''' 
异常处理
异常发生之后，异常之后的代码就不会执行了，如果想要代码正常运行，就要进行异常处理了。

2.1 什么是异常处理
python解释器检测到错误，触发异常（也允许程序员自己触发异常）。

程序员编写特定的代码，专门用来捕捉这个异常（这段代码与程序逻辑无关，与异常处理有关）。

如果捕捉成功则进入另外一个处理分支，执行你为其定制的逻辑，使程序不会崩溃，这就是异常处理。

2.2 为什么要进行异常处理
python解析器去执行程序，检测到了一个错误时，触发异常，异常触发后且没被处理的情况下，程序就在当前异常处终止，后面的代码不会运行，谁会去用一个运行着突然就崩溃的软件。

所以你必须提供一种异常处理机制来增强你程序的健壮性与容错性。 

2.3 如何进行异常处理
首先须知，异常是由程序的错误引起的，语法上的错误跟异常处理无关，必须在程序运行前就修正。

python为每一种异常导致了一个类型，然后提供了一种特定的语法结构来进行异常处理。
'''

''' 
2.3.1 基本语法
格式：

try:
     被检测的代码块
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
'''
# 例子
try:
    f = open('a.txt')
    g = (line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    f.close()
'''
next(g)会触发迭代f，依次next(g)就可以读取文件的一行行内容，无论文件a.txt有多大，同一时刻内存中只有一行内容。
提示：g是基于文件句柄f而存在的，因而只能在next(g)抛出异常StopIteration后才可以执行f.close()
'''
# 异常类智能用来处理指定的异常情况，如果非指定异常则无法处理。
s1 = 'hello'
try:
    int(s1)
except ValueError as e:
    print('代码执行报错，异常信息为：', e)

''' 
多分支
格式：

try:
     被检测的代码块
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
    ...
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
'''

''' 
从上向下报错的代码只要找到一个和报错类型相符的分支就执行这个分支中的代码，然后直接退出分支。
如果找不到能处理和报错类型相同的分支，会一直往下走，最后还是没有找到就会报错。
'''
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print('IndexError:', e)
except KeyError as e:
    print('KeyError:', e)
except ValueError as e:
    print('ValueError:', e)

''' 
万能异常
在python的异常中，有一个万能异常：Exception，他可以捕获任意异常，即：
'''
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print('Exception:', e)


''' 
异常的其他结构
格式：

try:
     被检测的代码块
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
    ...
except 异常类型：
     try中一旦检测到异常，就执行这个位置的逻辑
else:
    try内代码块没有异常则执行
finally:
    无论异常与否,都会执行该模块,通常是进行清理工作
'''
print('分割线'.center(50, '*'))
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print('IndexError:', e)
except KeyError as e:
    print('KeyError:', e)
except ValueError as e:
    print('ValueError:', e)
#except Exception as e:
#    print(e)
else:
    print('try内代码块没有异常则执行我')
finally:
    print('无论异常与否,都会执行该模块,通常是进行清理工作')

''' 
主动触发异常
'''
print('分割线'.center(50, '*'))
try:
    raise TypeError('类型错误')
except Exception as e:
    print(e) # 类型错误

''' 
自定义异常
'''
print('分割线'.center(50, '*'))
class EvaException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    raise EvaException('类型错误')
except EvaException as e:
    print(e)

''' 
什么时候使用异常处理
有的同学会这么想，学完了异常处理后，好强大，我要为我的每一段程序都加上try...except，干毛线去思考它会不会有逻辑错误啊，这样就很好啊。

try...except应该尽量少用，因为它本身就是你附加给你的程序的一种异常处理的逻辑，与你的主要的工作是没有关系的。
这种东西加的多了，会导致你的代码可读性变差，只有在有些异常无法预知的情况下，才应该加上try...except，其他的逻辑错误应该尽量修正。

异常的继承关系：
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning 
'''