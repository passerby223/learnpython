# coding: utf-8 
# @Time    : 2020/3/11 下午9:24
# @File    : 序列化_json模块_pickle模块.py
# @Author  : wenbin
# @Software: PyCharm
import json

''' 
序列化
什么叫序列化——将原本的字典、列表等内容转换成一个字符串的过程就叫做序列化。
1.1 为什么要有序列化
为什么要把其他数据类型转换成字符串?
因为能够在网络上传输的只能是bytes，
而能够存储在文件里的只有bytes和str。
比如，我们在python代码中计算的一个数据需要给另外一段程序使用，那我们怎么给？
现在我们能想到的方法就是存在文件里，然后另一个python程序再从文件里读出来。
但是我们都知道，对于文件来说是没有字典这个概念的，所以我们只能将数据转换成字典放到文件中。
你一定会问，将字典转换成一个字符串很简单，就是str(dic)就可以办到了，为什么我们还要学习序列化模块呢？
没错序列化的过程就是从dic 变成str(dic)的过程。现在你可以通过str(dic)，将一个名为dic的字典转换成一个字符串，
但是你要怎么把一个字符串转换成字典呢？
聪明的你肯定想到了eval()，如果我们将一个字符串类型的字典str_dic传给eval，就会得到一个返回的字典类型了。
eval()函数十分强大，但是eval是做什么的？官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果。
但是。强大的函数有代价。安全性是其最大的缺点。
想象一下，如果我们从文件中读出的不是一个数据结构，而是一句"删除文件"类似的破坏性语句，那么后果实在不堪设想。
而使用eval就要担这个风险。
所以，我们并不推荐用eval方法来进行反序列化操作(将str转换成python中的数据结构)
'''
dict1 = {'哈哈': 'haha', '呵呵': 'hehe'}
print(str(dict1))
print(type(str(dict1)))
''' 
序列化的目的
1、以某种存储形式使自定义对象持久化；
2、将对象从一个地方传递到另一个地方。
3、使程序更具维护性
str ————> 反序列化————> 数据结构
 ↑                       ↓
<--------序列化  <————————
'''

''' 
json模块
Json模块提供了四个功能：dumps、dump、loads、load。
导入json模块：
import json
'''
print('分割线'.center(50, '*'))
# loads和dumps
dict2 = {'哈哈': 'haha', '呵呵': 'hehe', '啦啦': 'lala'}
print('type(dict2):', type(dict2))
dict2_str = json.dumps(dict2, ensure_ascii=False)  # 序列化：将一个字典转换成一个字符串 json转换完的字符串类型的字典中的字符串是由""表示的
dict2_str1 = json.dumps(dict2, ensure_ascii=False)  # 序列化：将一个字典转换成一个字符串
print('dict2_str:', dict2_str)
print('dict2_str:', dict2_str1)
print('type(dict2_str):', type(dict2_str))
print('分割线'.center(50, '*'))
dict2_dict = json.loads(dict2_str)  # 反序列化：将一个字符串格式的字典转换成一个字典
print(dict2_dict, type(dict2_dict))
# 注意，要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示
# 如果是单引号会报错
# dict3 = "{'哈哈': 'haha', '呵呵': 'hehe', '啦啦': 'lala'}"
# dict3_dict = json.loads(dict3) # 报错：json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# print(dict3_dict)
print('分割线'.center(50, '*'))
list_dic = [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]
str_dic = json.dumps(list_dic, indent=2)  # 也可以处理嵌套的数据类型
print(type(str_dic), str_dic)  # <class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
list_dic2 = json.loads(str_dic)
print(type(list_dic2), list_dic2)  # <class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]

'''
load和dump
'''
print('分割线'.center(50, '*'))
f = open('json_file', 'w')
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
json.dump(dic, f)  # dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close()
f1 = open('json_file')
dic2 = json.load(f1)  # load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
f1.close()
print(type(dic2), dic2)

''' 
ensure_ascii关键字参数
如果``ensure_ascii''为false，则返回值可以包含在``obj''包含的字符串中的非ASCII字符。否则，所有此类字符都将以JSON字符串转义。
'''
print('分割线'.center(50, '*'))
f = open('file', 'w')
json.dump({'国籍': '中国'}, f)  # 文件内的内容为：{"\u56fd\u7c4d": "\u4e2d\u56fd"}
f.write('\n' + '分割线'.center(50, '*') + '\n')
json.dump({'国籍': '中国'}, f, ensure_ascii=False)  # 文件内的内容为：{"\u56fd\u7c4d": "\u4e2d\u56fd"}
f.write('\n' + '分割线'.center(50, '*') + '\n')
ret = json.dumps({'国籍': '中国'})
f.write(ret)
f.write('\n' + '分割线'.center(50, '*') + '\n')
ret = json.dumps({'国籍': '美国'}, ensure_ascii=False)
f.write(ret + '\n')
f.close()

r''' 
其他参数说明
Serialize obj to a JSON formatted str.(字符串表示的json对象) 
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key 
ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。) 
If check_circular is false, then the circular reference check for container types will be skipped and a circular reference will result in an OverflowError (or worse). 
If allow_nan is false, then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (NaN, Infinity, -Infinity). 
indent：应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json 
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。 
default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError. 
sort_keys：将数据根据keys的值进行排序。 
To use a custom JSONEncoder subclass (e.g. one that overrides the .default() method to serialize additional types), specify it with the cls kwarg; otherwise JSONEncoder is used.
'''

'''
json的格式化输出
'''
data = {'username': ['李华', '二愣子'], 'sex': 'male', 'age': 16}
json_dic2 = json.dumps(data, sort_keys=True, indent=2, separators=(',', ':'), ensure_ascii=False)
print(json_dic2)

''' 
pickle模块
用于序列化的两个模块：
json，用于字符串 和 python数据类型间进行转换。
pickle，用于python特有的类型 和 python的数据类型间进行转换。
pickle模块提供了四个功能：dumps、dump(序列化，存）、loads（反序列化，读）、load （不仅可以序列化字典，列表...可以把python中任意的数据类型序列化）。
'''
import pickle

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  # 一串二进制内容
dic2 = pickle.loads(str_dic)
print(dic2)  # 字典

print('分割线'.center(50, '*'))
import time

struct_time = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file', 'wb')
pickle.dump(struct_time, f)
f.close()
f = open('pickle_file', 'rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)