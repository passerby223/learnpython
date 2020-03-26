# coding: utf-8 
# @Time    : 2020/3/3 下午10:53
# @File    : file_test.py
# @Author  : wenbin
# @Software: PyCharm


# list1 = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
# with open('test.txt', mode='r') as file:
    # for i in list1:
    #     file.write(i + '\n')
    # a = 1
    # for i in file:
    #     print(i.strip('\n'))
    #     print(a)
    #     a += 1
    # a = file.readline()
    # b = file.readline()
    # c = file.readline()
    # d = file.readline()
    # print(a.rstrip('\n'))
    # print(b.rstrip('\n'))
    # print(c.rstrip('\n'))
    # print(d.rstrip('\n'))f = open("⼩娃娃", mode="r+", encoding="utf-8")
    # content = f.read()
    # f.write("麻花藤的最爱")
    # print(content)
    # f.flush()
    # f.close()
    # pass
'''
seek(n)：光标移动到n位置，注意，移动的单位是byte，所以如果是UTF-8的中⽂部分要
是3的倍数。
通常我们使⽤seek都是移动到开头或者结尾。
移动到开头: seek(0)
移动到结尾: seek(0,2) 　　seek的第⼆个参数表⽰的是从哪个位置进⾏偏移，默认是0，表
⽰开头，1表⽰当前位置，2表⽰结尾。
'''
# f = open("test1", mode="r+", encoding="utf-8")
# content = f.read()
# f.write("\n麻花藤的最爱")
# f.seek(0)  # 光标移动到开头
# print('content:', content)
# f.seek(0, 2)  # 光标移动到末尾
# content1 = f.read()
# print('content1:', content1)
# f.seek(0)  # 光标移动到开头
# f.write('啦啦啦哈哈哈') # 写⼊信息. 此时光标在9 中⽂3 * 3个 = 9
# index = f.tell()
# print(index)
# # 从当前光标读取到的内容
# content_index = f.read()
# print('从光标{}读取到的内容:{}'.format(index, content_index))
# # 光标移动到6位置
# f.seek(6)
# # 打印此时光标所在位置
# current_index = f.tell()
# print('此时光标所在位置:{}'.format(current_index))
# # 删除当前光标之后的所有内容
# f.truncate(9)
# '''
# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
# '''
# # f.flush()
# # 关闭文件
# f.close()
# ⽂件修改
# import os
# with open("hello", mode="r", encoding="utf-8") as f1, open("hello_new", mode="w", encoding="utf-8") as f2:
#     content = f1.read()
#     print(content)
#     new_content = content.replace("冰糖葫芦", "⼤⽩梨")
#     print(new_content)
#     f2.write(new_content)
# os.remove("hello") # 删除源⽂件
# os.rename("hello_new", "hello_new1") # 重命名新⽂件

# a = 10
# def func():
#     a = 40
#     b = 20
#     def abc():
#         print("哈哈")
#     print(a, b) # 这⾥使⽤的是局部作⽤域
#     print(globals()) # 打印全局作⽤域中的内容
#     print(locals()) # 打印局部作⽤域中的内容
#
# func()
# def fun1():
#     print(111)
# def fun2():
#     print(222)
#     fun1()
#
#
# fun2()
# print(111)
#
#
# # 函数的嵌套
# def fun2():
#     print(222)
#     def fun3():
#         print(666)
#     print(444)
#     fun3()
#     print(888)
# print(33)
# fun2()
# print(555)

# global使用
# a = 100
# def func1():
#     global a # 加了个global表示该func1方法里的局部变量a被重新声明为全部变量了
#     a = 5  # 对全局变量重新赋值
#     print(a)
#
# func1()
# print(a)  # 此时a的值已被重新赋值为5
#
# # 不使用global
# a = 100
# def func1():
#     a = 5
#     print(a)  # 5
#
# func1()
# print(a)  # 100

# lst = ["麻花藤", "刘嘉玲", "詹姆斯"]
# print(lst)  # ['麻花藤', '刘嘉玲', '詹姆斯']
# print(id(lst))
# def func1():
#     lst.append("⻢云云") # 对于可变数据类型可以直接进⾏修改不用用global来声明为全局变量在进行之后的操作
#     print(lst)  # ['麻花藤', '刘嘉玲', '詹姆斯', '⻢云云']
#     print(id(lst))
#
#
# func1()
# print(lst)  # ['麻花藤', '刘嘉玲', '詹姆斯', '⻢云云']
# print(id(lst))

''' 
加了nonlocal
30
30
不加nonlocal
30
20
'''
# a = 10
# def func1():
#     a = 20
#     def func2():
#         nonlocal a
#         a = 30
#         print(a)
#     func2()
#     print(a)
#
# func1()

''' 

'''
a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)

print(a)
fun_1()
print(a)