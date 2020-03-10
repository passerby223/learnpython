# coding: utf-8 
# @Time    : 2020/3/11 上午1:29
# @File    : random_time_sys_os.py
# @Author  : wenbin
# @Software: PyCharm
'''
random模块
'''
# import random
# '''
# 随机小数
# 取随机小数 : 数学计算。
# random() -> x in the interval [0, 1).
# '''
# print(random.random())
# '''
# 随机整数
# 取随机整数 : 在彩票，抽奖中有使用。
# randint():Return random integer in range [a, b], including both end points(包括两个端点).
# randrange():
# Choose a random item from range(start, stop[, step]).
#
#         This fixes the problem with randint() which includes the
#         endpoint; in Python this is usually not what you want.
#
#         """
#
#         # This code is a bit messy to make it fast for the
#         # common case while still doing adequate error checking.
# '''
# print(random.randint(1, 2))
# # print(random.randrange(1, 3))
# print(random.randrange(1, 20, 2))
# '''
# 从列表中随机抽取值
# 从一个列表中随机抽取值 ，例如抽奖。
# '''
# list1 = [1, 8, 78, ['a', 'b'], (5, 47), {"key": "value"}, "dnf", True, False, 3.1415926]
# print(random.choice(list1))
# print(random.sample(list1, 4)) # 随机从一个序列中选择4个元素返回一个新列表。
# print(random.sample(range(1, 100000), 100))
# '''
# 打乱列表顺序
# 打乱一个列表的顺序，在原列表的基础上直接进行修改，节省空间，例如洗牌。
# '''
# print('未打乱原有顺序前的list1为：{}'.format(list1))
# random.shuffle(list1)
# print('打乱原有顺序后的list1为：{}'.format(list1))

''' 
time模块
time模块主要是用来和时间打交道的
导入的是time模块，格式是：
import time
'''
import time
# 时间格式
'''
'2018-8-20' '2018.8.20' 字符串数据类型     格式化时间 - 给人看的
结构化时间
1534732642.617272  浮点型数据类型,以s为单位 时间戳时间 - 给机器计算用的
1970 1 1 0:0:0
'''
''' 
时间戳时间
'''
print(time.time())  # 1583862407.3392875
''' 
格式化时间
'''
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 2020-03-11 01:48:19
print(time.strftime('%y-%m-%d %H:%M:%S')) # 20-03-11 01:49:02
print(time.strftime('%c')) # Wed Mar 11 01:49:34 2020
''' 
结构化时间
localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)
Convert seconds since the Epoch to a time tuple expressing local time.
When 'seconds' is not passed in, convert the current time instead.
'''
struct_time = time.localtime()  # 北京时间
struct_time1 = time.localtime(3)  # 北京时间
print(struct_time)  # time.struct_time(tm_year=2020, tm_mon=3, tm_mday=11, tm_hour=1, tm_min=54, tm_sec=55, tm_wday=2, tm_yday=71, tm_isdst=0)
print(struct_time1)  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=3, tm_wday=3, tm_yday=1, tm_isdst=0)
print(struct_time.tm_year) # 2020
print(struct_time.tm_zone) # CST
print(struct_time.tm_hour) # 1
''' 
时间戳换成字符串时间
'''
# 当前时间戳
current_timestamp = time.time()
print(current_timestamp)
struct_time = time.localtime()
print(time.gmtime(1500000000))
local_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
print(local_time)
print('分割线'.center(50, '*'))
''' 
字符串时间转时间戳
'''
struct_time = time.strptime('2018-8-8','%Y-%m-%d')
print(struct_time)
res = time.mktime(struct_time)
print(res)

''' 
sys模块
sys是和Python解释器打交道的
导入的是sys模块，格式是：
import sys
'''
'''
argv
'''
import sys
# 返回一个列表, 列表中的第一个参数是当前py文件(也叫模块)所在路径
# 控制台输入命令运行当前程序：python3 basis/random_time_sys_os.py admin 123456
# print(sys.argv)  # ['basis/random_time_sys_os.py', 'admin', '123456']
# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr == 'admin' and pwd == '123456':
#     print('登录成功') # 登录成功
# else:
#     exit()

''' 
path
模块是存在解释器里的么?不是。
模块应该是存在硬盘上，
但是我在使用的时候 import --> 这个模块才到内存中。
一个模块能否被顺利的导入，全看sys.path下面有没有这个模块所在的。
自定义模块的时候，导入模块的时候，还需要再关注 sys.path。
'''
print('分割线'.center(50, '*'))
print(sys.modules)  # 是我们导入到内存中的所有模块的名字 : 这个模块的内存地址；输出见下一行
print(sys.modules['re'].findall('\d','abc126')) # ['1', '2', '6']
print("sys.modules['re']：{}".format(sys.modules['re'])) # sys.modules['re']：<module 're' from '/usr/lib/python3.6/re.py'>
'''
{'builtins': <module 'builtins' (built-in)>, 'sys': <module 'sys' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, 'encodings': <module 'encodings' from '/usr/lib/python3.6/encodings/__init__.py'>, 'codecs': <module 'codecs' from '/usr/lib/python3.6/codecs.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib/python3.6/encodings/aliases.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib/python3.6/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from '/home/wenbin/PycharmProjects/learnpython/basis/random_time_sys_os.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib/python3.6/encodings/latin_1.py'>, 'io': <module 'io' from '/usr/lib/python3.6/io.py'>, 'abc': <module 'abc' from '/usr/lib/python3.6/abc.py'>, '_weakrefset': <module '_weakrefset' from '/usr/lib/python3.6/_weakrefset.py'>, 'site': <module 'site' from '/usr/lib/python3.6/site.py'>, 'os': <module 'os' from '/usr/lib/python3.6/os.py'>, 'errno': <module 'errno' (built-in)>, 'stat': <module 'stat' from '/usr/lib/python3.6/stat.py'>, '_stat': <module '_stat' (built-in)>, 'posixpath': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>, 'genericpath': <module 'genericpath' from '/usr/lib/python3.6/genericpath.py'>, 'os.path': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>, '_collections_abc': <module '_collections_abc' from '/usr/lib/python3.6/_collections_abc.py'>, '_sitebuiltins': <module '_sitebuiltins' from '/usr/lib/python3.6/_sitebuiltins.py'>, 'sysconfig': <module 'sysconfig' from '/usr/lib/python3.6/sysconfig.py'>, '_sysconfigdata_m_linux_x86_64-linux-gnu': <module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>, '_bootlocale': <module '_bootlocale' from '/usr/lib/python3.6/_bootlocale.py'>, '_locale': <module '_locale' (built-in)>, 'types': <module 'types' from '/usr/lib/python3.6/types.py'>, 'functools': <module 'functools' from '/usr/lib/python3.6/functools.py'>, '_functools': <module '_functools' (built-in)>, 'collections': <module 'collections' from '/usr/lib/python3.6/collections/__init__.py'>, 'operator': <module 'operator' from '/usr/lib/python3.6/operator.py'>, '_operator': <module '_operator' (built-in)>, 'keyword': <module 'keyword' from '/usr/lib/python3.6/keyword.py'>, 'heapq': <module 'heapq' from '/usr/lib/python3.6/heapq.py'>, '_heapq': <module '_heapq' (built-in)>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from '/usr/lib/python3.6/reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'weakref': <module 'weakref' from '/usr/lib/python3.6/weakref.py'>, 'collections.abc': <module 'collections.abc' from '/usr/lib/python3.6/collections/abc.py'>, 'importlib': <module 'importlib' from '/usr/lib/python3.6/importlib/__init__.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from '/usr/lib/python3.6/warnings.py'>, 'importlib.util': <module 'importlib.util' from '/usr/lib/python3.6/importlib/util.py'>, 'importlib.abc': <module 'importlib.abc' from '/usr/lib/python3.6/importlib/abc.py'>, 'importlib.machinery': <module 'importlib.machinery' from '/usr/lib/python3.6/importlib/machinery.py'>, 'contextlib': <module 'contextlib' from '/usr/lib/python3.6/contextlib.py'>, 'lazr': <module 'lazr' (namespace)>, 'google': <module 'google' (namespace)>, 'zope': <module 'zope' (namespace)>, 'virtualenvwrapper': <module 'virtualenvwrapper' (namespace)>, 'sitecustomize': <module 'sitecustomize' from '/usr/lib/python3.6/sitecustomize.py'>, 'apport_python_hook': <module 'apport_python_hook' from '/usr/lib/python3/dist-packages/apport_python_hook.py'>, 'time': <module 'time' (built-in)>, '_strptime': <module '_strptime' from '/usr/lib/python3.6/_strptime.py'>, 'locale': <module 'locale' from '/usr/lib/python3.6/locale.py'>, 're': <module 're' from '/usr/lib/python3.6/re.py'>, 'enum': <module 'enum' from '/usr/lib/python3.6/enum.py'>, 'sre_compile': <module 'sre_compile' from '/usr/lib/python3.6/sre_compile.py'>, '_sre': <module '_sre' (built-in)>, 'sre_parse': <module 'sre_parse' from '/usr/lib/python3.6/sre_parse.py'>, 'sre_constants': <module 'sre_constants' from '/usr/lib/python3.6/sre_constants.py'>, 'copyreg': <module 'copyreg' from '/usr/lib/python3.6/copyreg.py'>, 'calendar': <module 'calendar' from '/usr/lib/python3.6/calendar.py'>, 'datetime': <module 'datetime' from '/usr/lib/python3.6/datetime.py'>, 'math': <module 'math' (built-in)>, '_datetime': <module '_datetime' (built-in)>}
'''

import os
print('分割线'.center(50, '*'))
''' 
os模块
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.system("bash command")  运行shell命令，直接显示
os.popen("bash command).read()  运行shell命令，获取执行结果
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.path
os.path.abspath(path) 返回path规范化的绝对路径
os.path.split(path) 将path分割成目录和文件名二元组返回 
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 
os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小
'''

print('分割线'.center(50, '*'))
''' 
stat结构
注意：os.stat('path/filename')  获取文件/目录信息 的结构说明
stat 结构:
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''
print(os.stat('.' + os.sep + 'random_time_sys_os.py'))

print('分割线'.center(50, '*'))
''' 
os模块的属性
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
'''
print(os.sep)
print(os.linesep)
print(os.pathsep)
print(os.name)