# coding: utf-8 
# @Time    : 2020/3/9 上午12:21
# @File    : 正则练习.py
# @Author  : wenbin
# @Software: PyCharm


import re

# 正则匹配规则
'''
1. 正则表达式
1.1 正则表达式是什么
正则表达式本身也和python没有什么关系，就是匹配字符串内容的一种规则。
官方定义：正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
一说规则我已经知道你很晕了，现在就让我们先来看一些实际的应用。在线测试工具 http://tool.chinaz.com/regex/
首先你要知道的是，谈到正则，就只和字符串相关了。在我给你提供的工具中，你输入的每一个字都是一个字符串。
其次，如果在一个位置的一个值，不会出现什么变化，那么是不需要规则的。
比如你要用"1"去匹配"1"，或者用"2"去匹配"2"，直接就可以匹配上。这连python的字符串操作都可以轻松做到。
那么在之后我们更多要考虑的是在同一个位置上可以出现的字符的范围。
1.2 正则表达式的匹配规则
字符：x
含义：代表的是字符x
例如：匹配规则为 "a"，那么需要匹配的字符串内容就是 ”a”

字符：\\
含义：代表的是反斜线字符'\'
例如：匹配规则为"\\" ，那么需要匹配的字符串内容就是 ”\”

字符：\t
含义：制表符
例如：匹配规则为"\t" ，那么对应的效果就是产生一个制表符的空间

字符：\n
含义：换行符
例如：匹配规则为"\n"，那么对应的效果就是换行,光标在原有位置的下一行

字符：\r
含义：回车符
例如：匹配规则为"\r" ，那么对应的效果就是回车后的效果,光标来到下一行行首

字符类：[abc]
含义：代表的是字符a、b 或 c
例如：匹配规则为"[abc]" ，那么需要匹配的内容就是字符a，或者字符b，或字符c的一个

字符类：[^abc]
含义：代表的是除了 a、b 或 c以外的任何字符
例如：匹配规则为"[^abc]"，那么需要匹配的内容就是不是字符a，或者不是字符b，或不是字符c的任意一个字符

字符类：[a-zA-Z]
含义：代表的是a 到 z 或 A 到 Z，两头的字母包括在内
例如：匹配规则为"[a-zA-Z]"，那么需要匹配的是一个大写或者小写字母

字符类：[0-9]
含义：代表的是 0到9数字，两头的数字包括在内
例如：匹配规则为"[0-9]"，那么需要匹配的是一个数字

字符类：[a-zA-Z_0-9]
含义：代表的字母或者数字或者下划线(即单词字符)
例如：匹配规则为" [a-zA-Z_0-9] "，那么需要匹配的是一个字母或者是一个数字或一个下滑线

预定义字符类：.
含义：代表的是任何字符
例如：匹配规则为" . "，那么需要匹配的是一个任意字符。如果，就想使用 . 的话，使用匹配规则"\\."来实现

预定义字符类：\d
含义：代表的是 0到9数字，两头的数字包括在内，相当于[0-9]
例如：匹配规则为"\d "，那么需要匹配的是一个数字

预定义字符类：\w
含义：代表的字母或者数字或者下划线(即单词字符)，相当于[a-zA-Z_0-9]
例如：匹配规则为"\w "，，那么需要匹配的是一个字母或者是一个数字或一个下滑线

边界匹配器：^
含义：代表的是行的开头
例如：匹配规则为^[abc][0-9]$ ，那么需要匹配的内容从[abc]这个位置开始, 相当于左双引号

边界匹配器：$
含义：代表的是行的结尾
例如：匹配规则为^[abc][0-9]$ ，那么需要匹配的内容以[0-9]这个结束, 相当于右双引号

边界匹配器：\b
含义：代表的是单词边界
例如：匹配规则为"\b[abc]\b" ，那么代表的是字母a或b或c的左右两边需要的是非单词字符([a-zA-Z_0-9])

数量词：X?
含义：代表的是X出现一次或一次也没有
例如：匹配规则为"a?"，那么需要匹配的内容是一个字符a，或者一个a都没有

数量词：X*
含义：代表的是X出现零次或多次
例如：匹配规则为"a*" ，那么需要匹配的内容是多个字符a，或者一个a都没有

数量词：X+
含义：代表的是X出现一次或多次
例如：匹配规则为"a+"，那么需要匹配的内容是多个字符a，或者一个a

数量词：X{n}
含义：代表的是X出现恰好 n 次
例如：匹配规则为"a{5}"，那么需要匹配的内容是5个字符a

数量词：X{n,}
含义：代表的是X出现至少 n 次
例如：匹配规则为"a{5, }"，那么需要匹配的内容是最少有5个字符a

数量词：X{n,m}
含义：代表的是X出现至少 n 次，但是不超过 m 次

例如：匹配规则为"a{5,8}"，那么需要匹配的内容是有5个字符a 到 8个字符a之间
'''

'''
findall : 匹配所有，每一项都是列表中的一个元素
'''
result = re.findall('\d+', '784dsfjdsj45gfdg2')
result1 = re.findall('\d', '784dsfjdsj45gfdg2')
print(result)  # ['784', '45', '2']
print(result1)  # ['7', '8', '4', '4', '5', '2']
''' 
search
search : 只匹配从左到右的第一个，得到的不是直接的结果，而是一个变量，通过这个变量的group方法来获取结果。
如果没有匹配到，会返回None，使用group会报错。
'''
result2 = re.search('\d+', '784dsfjdsj45gfdg2')
result3 = re.search('\d', '784dsfjdsj45gfdg2')
result4 = re.search('\d', '我的dsfjdsjgfdg')
print(result2)  # <_sre.SRE_Match object; span=(0, 3), match='784'>
print(result2.group())  # 784
print(result3.group())  # 784

print(result4)  # None
# print(result4.group())# AttributeError: 'NoneType' object has no attribute 'group'

''' 
match
match：从头开始匹配,相当于search中的正则表达式加上一个^。
'''
result5 = re.match('\d+', '172sjkhk按实际花费928')
result6 = re.match('\d+', 'l就72sjkhk按实际花费928')
print(result5)  # <_sre.SRE_Match object; span=(0, 3), match='172'>
print(result5.group())  # 172
print(result6)  # None
# print(result6.group())# AttributeError: 'NoneType' object has no attribute 'group'

''' 
字符串处理的扩展
'''
# split：切割
s = 'alex|taibai|egon'
s1 = 'alex|taibai|egon|'
print('s', s.split('|'))  # s ['alex', 'taibai', 'egon']
print('s1', s1.split('|'))  # s1 ['alex', 'taibai', 'egon', '']
s2 = 'alex83taibai40egon'
s3 = 'alex83taibai40egon25'
s4 = 'alex8385taibai4012egon25'
result7 = re.split('\d+', s2)
result8 = re.split('\d+', s3)
result9 = re.split('\d', s4)
print('result7', result7)  # result7 ['alex', 'taibai', 'egon']
print('result8', result8)  # result8 ['alex', 'taibai', 'egon', '']
print('result9', result9)  # result9 ['alex', '', '', '', 'taibai', '', '', '', 'egon', '', '']

# sub：替换
result10 = re.sub('\d+', '[替换标记]', 'alex83taibai40e1gon25')
result11 = re.sub('\d', '[替换标记]', 'alex83taibai40e1gon25')
print(result10)
print(result11)
result11 = re.sub('\d+', '[替换标记]', 'alex835taibai40egon25', 1)  # 旧，新，需要替换的，次数
result12 = re.sub('\d', '[替换标记]', 'alex835taibai40egon25', 2)  # 旧，新，需要替换的，次数
print(result11)
print(result12)

# subn：返回一个元组,第二个元素是替换的次数
result13 = re.subn('\d+', '[替换标记]', 'alex83taibai40e1gon25')
result14 = re.subn('\d', '[替换标记]', 'alex83taibai40e1gon25')
print(result13)
print(result14)

''' 
re模块的进阶：时间/空间
compile 节省你使用正则表达式解决问题的时间。
编译正则表达式，编译成字节码。
在多次使用的过程中，不会多次编译。
'''
result14 = re.compile('\d+')   # 已经完成编译了  编译正则表达式模式，返回模式对象
result15 = re.compile('\d')   # 已经完成编译了  编译正则表达式模式，返回模式对象
print(result14) # re.compile('\\d+')
print(result15) # re.compile('\\d')
res1 = result14.findall('alex83taibai40egon25')
res2 = result15.findall('alex83taibai40egon25')
print(res1)# ['83', '40', '25']
print(res2)# ['8', '3', '4', '0', '2', '5']
res3 = result14.search('sjkhk172按实际花费928')
res4 = result15.search('sjkhk172按实际花费928')
print(res3.group())# 172
print(res4.group())# 1

''' 
方法总结
findall 返回列表 找所有的匹配项
search  匹配就 返回一个变量,通过group取匹配到的第一个值,不匹配就返回None,group会报错
match   相当于search的正则表达式中加了一个'^'
spilt   返回列表,按照正则规则切割,默认匹配到的内容会被切掉
sub/subn 替换,按照正则规则去寻找要被替换掉的内容,subn返回元组,第二个值是替换的次数
compile  编译一个正则表达式,用这个结果去search match findall finditer 能够节省时间
finditer 返回一个迭代器,所有的结果都在这个迭代器中,需要通过循环+group的形式取值 能够节省内存
'''
print('分组的使用'.center(50, '*'))
# 分组的使用
s = '<a>wahaha</a>'  # 标签语言 html 网页
ret = re.search('<(\w+)>(\w+)</(\w+)>', s)
print(ret.group())  # 所有的结果
print(ret.group(1))  # 数字参数代表的是取对应分组中的内容
print(ret.group(2))
print(ret.group(3))
# 为了findall也可以顺利取到分组中的内容，有一个特殊的语法，就是优先显示分组中的内容。
s = '<a>wahaha</a>'
ret = re.findall('(\w+)', s)
print(ret)
ret = re.findall('>(\w+)<', s)
print(ret)
# 取消分组优先(?:正则表达式)
ret = re.findall('\d+(\.\d+)?', '1.234*4')
print(ret)
ret = re.findall('\d+(?:\.\d+)?', '1.234*4')
print(ret)

''' 
对于正则表达式来说，有些时候我们需要进行分组，来整体约束某一组字符出现的次数。
(\.[\w]+)?
对于python语言来说，分组可以帮助你更好更精准的找到你真正需要的内容。
<(\w+)>(\w+)</(\w+)>
python 和 正则表达式 之间的特殊的约定。
分组命名：
(?P<这个组的名字>正则表达式)
'''
s = '<a>wahaha</a>'
ret = re.search('>(?P<con>\w+)<', s)
print(ret.group(1))
print(ret.group('con'))

s = '<a>wahaha</a>'
pattern = '<(\w+)>(\w+)</(\w+)>'
ret = re.search(pattern, s)
print(ret.group(1) == ret.group(3))

# 使用前面的分组, 要求使用这个名字的分组和前面同名分组中的内容匹配的必须一致
pattern = '<(?P<tab>\w+)>(\w+)</(?P=tab)>'
ret = re.search(pattern, s)
print(ret)


