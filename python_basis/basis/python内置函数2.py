# coding: utf-8 
# @Time    : 2020/3/8 下午7:36
# @File    : python内置函数2.py
# @Author  : wenbin
# @Software: PyCharm

''''
1. lamda匿名函数
为了解决⼀些简单的需求⽽设计的⼀句话函数
'''
# 计算n的n次⽅
# def func(n):
#     return n**n
# print(func(2))
#
# f = lambda n: n**n
# print(f(2))
''' 
lambda表⽰的是匿名函数，不需要⽤def来声明，⼀句话就可以声明出⼀个函数。
语法:
函数名 = lambda 参数: 返回值
注意:
1. 函数的参数可以有多个，多个参数之间⽤逗号隔开
2. 匿名函数不管多复杂，只能写⼀⾏，且逻辑结束后直接返回数据
3. 返回值和正常的函数⼀样，可以是任意数据类型
匿名函数并不是说⼀定没有名字，这⾥前⾯的变量就是⼀个函数名，说他是匿名原因是我们通过__name__查看的时候是没有名字的，统⼀都叫lambda，
在调⽤的时候没有什么特别之处，像正常的函数调⽤即可。
'''

# lambda 函数求正方形面积
# try:
#     rectangle_side_long = int(input('请输入正方形的边长：'))
#     if rectangle_side_long <=0 :
#         print('输入边长格式不正确,请输入正整数!')
#     else:
#         f1 = lambda side_length: rectangle_side_long ** 2
#         print('边长为{}的正方形的面积为{}'.format(rectangle_side_long, f1(rectangle_side_long)))
# except Exception:
#     print('输入边长格式不正确,请输入正整数!')

# lambda 函数求长方形面积
# try:
#     rectangle_side_long = int(input('请输入长方形的长：'))
#     rectangle_side_width = int(input('请输入长方形的宽：'))
#     if rectangle_side_long > 0 and rectangle_side_width > 0:
#         f1 = lambda side_long, side_width: rectangle_side_long * rectangle_side_width
#         print('长为{}宽为{}的长方形的面积为{}'.format(rectangle_side_long, rectangle_side_width, f1(rectangle_side_long, rectangle_side_width)))
#     else:
#         print('输入数据格式不正确,请输入正整数!')
# except Exception:
#     print('输入格式不正确,请输入正整数!')

''' 
sorted()
排序函数。
语法:
sorted(Iterable, key=None, reverse=False)
　　Iterable: 可迭代对象
　　key: 排序规则(排序函数)，在sorted内部会将可迭代对象中的每⼀个元素传递给这个函数的参数，根据函数运算的结果进⾏排序
　　reverse: 是否是倒叙，True: 倒叙，False: 正序
'''
# list1 = [1, 59, 9, 46, 1, 61, 323, 165, 564, 61, 6, 654, 655, 165]
# dict1 = {5: 8, 9: 7, 18: '34', 2: '哈哈'}
# sort方法直接在原可迭代对象上进行排序操作
# list1.sort(reverse=True) # 倒序排列
# list1.sort() # 正序排列
# print(list1)
# sorted方法不在在原可迭代对象上进行排序，返回一个新列表，其中包含迭代中所有项目的升序排列。
# 可以提供自定义键功能以自定义排序顺序，并且可以设置反向标志以按降序请求结果
# list_sorted = sorted(list1, reverse=True)
# dict_sorted1 = sorted(dict1)
# dict_sorted2 = sorted(dict1, reverse=True)
# print(list_sorted)
# print(dict_sorted1)# 默认以字典的 key为标准进行排序
# print(dict_sorted2)# 默认以字典的 key为标准进行排序


# sorted方法中key参数的使用
# 根据字符串⻓度进⾏排序
# lst = ["麻花藤", "冈本次郎", "中央情报局", "狐仙"]
#
# # 计算字符串⻓度
# def func(s):
#     return len(s)
# print(sorted(lst, key=func))
#
#
# # 根据字符串⻓度进⾏排序
# lst = ["麻花藤", "冈本次郎", "中央情报局", "狐仙"]
#
# # 计算字符串⻓度
# def func(s):
#     return len(s)
#
# print(sorted(lst, key=lambda s: len(s)))
#
# lst = [{"id":1, "name":'alex', "age":18}, {"id":2, "name":'wusir', "age":16}, {"id":3, "name":'taibai', "age":17}]
# # 按照年龄对学⽣信息进⾏排序
# print(sorted(lst, key=lambda e: e['age'], reverse=True))


# filter()
# 筛选函数
# 语法:
# filter(function. Iterable)
# 　　function: ⽤来筛选的函数，在filter中会⾃动的把iterable中的元素传递给function，然后根据function返回的True或者False来判断是否保留此项数据
# 　　Iterable: 可迭代对象

# 求出list1列表中长度为4的字符串
# list1 = ['我', '就是', '一个很', '厉害的人', '我说的对吗']
# a = filter(lambda s: len(s)==4, list1)
# print(list(a))

# lst = [1,2,3,4,5,6,7]
# ll = filter(lambda x: x%2==0, lst) # 筛选所有的偶数
# print(ll)
# print(list(ll))
#
# lst = [{"id":1, "name":'alex', "age":18}, {"id":2, "name":'wusir', "age":16}, {"id":3, "name":'taibai', "age":17}]
# fl = filter(lambda e: e['age'] > 16, lst) # 筛选年龄⼤于16的数据
# print(list(fl))

# map()
# 映射函数
# 语法:
# map(function, iterable) 可以对可迭代对象中的每⼀个元素进⾏映射，分别取执⾏function
# 创建一个迭代器，该迭代器使用每个可迭代对象的参数来计算函数。当最短的迭代次数用尽时停止。

# 计算列表中每个元素的平⽅ ,返回新列表
# def func(e):
#     return e*e
# mp = map(func, [1, 2, 3, 4, 5])
# print(mp)
# print(list(mp))
# # lambda 形式
# mp1 = map(lambda s: s**2, [1, 3, 5, 7, 9])
# print(mp1)
# print(list(mp1))
# # 计算两个列表相同位置的数据的和
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [2, 4, 6, 8, 10]
# print(list(map(lambda x, y: x+y, lst1, lst2)))

# 递归
# 在函数中调⽤函数本⾝，就是递归
# def func():
#     print("我是谁")
#     func()
# func()  # RecursionError: maximum recursion depth exceeded while calling a Python object
# 在python中递归的深度最⼤到998
# def foo(n):
#     print('n:', n)
#     n += 1
#     foo(n)
# foo(1)
# 递归的应⽤:
# 我们可以使⽤递归来遍历各种树形结构，比如我们的⽂件夹系统，可以使⽤递归来遍历该⽂件夹中的所有⽂件。
# import os
# def read(filepath, n):
#     files = os.listdir(filepath) # 获取到当前⽂件夹中的所有⽂件
#     for fi in files: # 遍历⽂件夹中的⽂件, 这⾥获取的只是本层⽂件名
#         fi_d = os.path.join(filepath,fi) # 加⼊⽂件夹 获取到⽂件夹+⽂件
#         if os.path.isdir(fi_d): # 如果该路径下的⽂件是⽂件夹
#             print("\t"*n, fi)
#             read(fi_d, n+1) # 继续进⾏相同的操作
#         else:
#             print("\t"*n, fi) # 递归出⼝. 最终在这⾥隐含着return
#
# #递归遍历⽬录下所有⽂件
# read('../', 0)

# 二分查找
# ⼆分查找，每次能够排除掉⼀半的数据，查找的效率非常⾼，但是局限性比较⼤，必须是有
# 序序列才可以使⽤⼆分查找。
# 要求: 查找的序列必须是有序序列。

# 判断n是否在lst中出现. 如果出现请返回n所在的位置
# ⼆分查找---⾮递归算法
lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
n = 567
left = 0
right = len(lst) - 1
count = 1
while left <= right:
    middle = (left + right) // 2
    if n < lst[middle]:
        right = middle - 1
    elif n > lst[middle]:
        left = middle + 1
    else:
        print(count)
        print(middle)
        break
    count = count + 1
else:
    print("不存在")

print('分割线'.center(30, '*'))
# 普通递归版本⼆分法
def binary_search(n, left, right):
    if left <= right:
        middle = (left+right) // 2
        if n < lst[middle]:
            right = middle - 1
        elif n > lst[middle]:
            left = middle + 1
        else:
            return middle
        return binary_search(n, left, right) # 这个return必须要加. 否则接收到的永远是None.
    else:
        return -1

print(binary_search(567, 0, len(lst)-1))

# 另类⼆分法, 很难计算位置.
def binary_search(ls, target):
    left = 0
    right = len(ls) - 1
    if left > right:
        print("不在这⾥")
    middle = (left + right) // 2
    if target < ls[middle]:
        return binary_search(ls[:middle], target)
    elif target > ls[middle]:
        return binary_search(ls[middle+1:], target)
    else:
        print("在这⾥")

binary_search(lst, 567)
