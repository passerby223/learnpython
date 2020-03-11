# coding: utf-8 
# @Time    : 2020/3/11 下午11:30
# @File    : 继承.py
# @Author  : wenbin
# @Software: PyCharm

class Alipay:
    '''
    支付宝支付
    '''

    def pay(self, money):
        print('支付宝支付了%s元' % money)


class Applepay:
    '''
    apple pay支付
    '''

    def pay(self, money):
        print('apple pay支付了%s元' % money)


def pay(payment, money):
    '''
    支付函数，总体负责支付
    对应支付的对象和要支付的金额
    '''
    payment.pay(money)


p = Alipay()
pay(p, 200)
