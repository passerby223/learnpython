# coding: utf-8 
# @Time    : 2020/3/4 下午10:56
# @File    : iterator_test.py
# @Author  : wenbin
# @Software: PyCharm

# # 用协程实现的生产者-消费者模型
# def producer(c):
#     '''生产者'''
#     n = 0
#     while n < 5:
#         n += 1
#         print('producer {}'.format(n))
#         r = c.send(n)
#         print('consumer return {}'.format(r))
#
#
# def consumer():
#     '''消费者'''
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('consumer {} '.format(n))
#         r = 'ok'
#
# def gen():
#     for i in range(10):
#         yield i
#         # print(i)
#
# if __name__ == '__main__':
#     print(gen())
#     for j in gen():
#         print(j)
#     # c = consumer()
#     # next(c)  # 启动consumer
#     # producer(c)

# lst = [1,2,3]
# lst_iter = lst.__iter__()
# while True:
#     try:
#         i = lst_iter.__next__()
#         print(i)
#     except StopIteration:
#         break

# def func():
#     print("111")
#     yield 222
#     print("333")
#     yield 444
# gener = func()
# ret = gener.__next__()
# print(ret)
# ret2 = gener.__next__()
# print(ret2)
# ret3 = gener.__next__() # 最后⼀个yield执⾏完毕. 再次__next__()程序报错, 也就是说. 和return⽆关了.
# print(ret3)

# def cloth():
#     for i in range(1, 11):
#         yield "⾐服"+str(i)
# cl = cloth()
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())  # 最后⼀个yield执⾏完毕. 再次__next__()程序报错,最大只能渠道10

'''
send和__next__()区别:
1. send和next()都是让⽣成器向下走⼀次。
2. send可以给上⼀个yield的位置传递值，不能给最后⼀个yield发送值，在第⼀次执⾏⽣成器代码的时候不能使⽤send()。
⽣成器可以使⽤for循环来循环获取内部的元素:
'''
# def eat():
#     print("我吃什么啊")
#     a = yield "馒头"
#     print("a=",a)
#     b = yield "⼤饼"
#     print("b=",b)
#     c = yield "⾲菜盒⼦"
#     print("c=",c)
#     yield "GAME OVER"
#
# gen = eat() # 获取⽣成器
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.send("胡辣汤")
# print(ret2)
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send("猫粮")
# print(ret4)
'''
打印：
我吃什么啊
馒头
a= 胡辣汤
⼤饼
b= 狗粮
⾲菜盒⼦
c= 猫粮
GAME OVER
'''

''' 
获取1-100之间所有的偶数,保存到一个列表中
'''
# # 方法1
# list1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list1)
# # 方法2
# list2_generator = (j for j in range(1, 101) if j % 2 == 0)
# list2 = []
# for k in list2_generator:
#     list2.append(k)
# print(list2)

# # 寻找名字中带有两个e的⼈的名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven','Joe'], ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# # 方法1 双重for循环
# print('方法1-->双重for循环'.center(30, '*'))
# names_with_two_e = []
# for i in names:
#     for j in i:
#         if j.count('e') == 2:
#             names_with_two_e.append(j)
# print(names_with_two_e)
# # 方法2 列表推导式
# print('方法2-->列表推导式'.center(30, '*'))
# names_with_two_e1 = [n for m in names for n in m if n.count('e') == 2]
# print(names_with_two_e1)
#
# # 方法3 生成器表达式
# print('方法3-->生成器表达式'.center(30, '*'))
# names_with_two_e_generator = (n for m in names for n in m if n.count('e') == 2)
# names_with_two_e_generator_list = []
# for o in names_with_two_e_generator:
#     names_with_two_e_generator_list.append(o)
# print(names_with_two_e_generator_list)
# '''
# ⽣成器表达式和列表推导式的区别:
# 1. 列表推导式比较耗内存，⼀次性加载，⽣成器表达式⼏乎不占⽤内存，使⽤的时候才分配和使⽤内存。
# 2. 得到的值不⼀样，列表推导式得到的是⼀个列表，⽣成器表达式获取的是⼀个⽣成器。
# 举个栗⼦。
# 同样⼀篮⼦鸡蛋，列表推导式: 直接拿到⼀篮⼦鸡蛋。⽣成器表达式: 拿到⼀个老⺟鸡，需要鸡蛋就给你下鸡蛋。
# ⽣成器的惰性机制: ⽣成器只有在访问的时候才取值，说⽩了，你找他要他才给你值，不找他要，他是不会执⾏的。
# ⽣成器，要值得时候才拿值。
# '''
# def func():
#     print(111)
#     yield 222
#
# g = func() # ⽣成器g
# g1 = (i for i in g) # ⽣成器g1. 但是g1的数据来源于g
# g2 = (i for i in g1) # ⽣成器g2. 来源g1
#
# print(list(g)) # 获取g中的数据. 这时func()才会被执⾏. 打印111.获取到222. g完毕.
# print(list(g1)) # [] 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
# print(list(g2)) # [] 和g1同理
#
# # 把字典中的key和value互换位置
# dict1 = {"name": "Tom", "age": 21}
# new_dict1 = {dict1[key]:key for key in dict1}
# print(new_dict1)


''' 
总结: 
推导式有，列表推导式，字典推导式，集合推导式，没有元组推导式。
⽣成器表达式:
(结果 for 变量 in 可迭代对象 if 条件筛选)  # 注意生成表达式用的是括号
⽣成器表达式可以直接获取到⽣成器对象，⽣成器对象可以直接进⾏for循环，⽣成器具有惰性机制。
'''