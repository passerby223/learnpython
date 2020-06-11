# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/11 下午8:33
# @Author    : ABC
# @FileName  : global_error_handle.py
from sqlite3 import DatabaseError

from flask import Flask, render_template, abort

app = Flask(__name__)

'''
全局错误处理方法(一)
在每个错误处理函数上使用装饰器进行绑定
'''


@app.route("/", endpoint='home')
def home():
    5 / 0
    return "这是home首页!"


# # 全局错误处理——>处理404
# @app.errorhandler(404)
# def error404(error):
#     return render_template('error_404.html')
#     # return error
#
#
# # 全局错误处理——>处理500
#
# @app.errorhandler(500)
# def error500(error):
#     return render_template('error_500.html')
#     # return error


'''
全局错误处理方法(二)：使用register_error_handler()方法集中处理
适用场景：需要处理的错误过多需要集中管理时。不过一般都是使用装饰器注册的方式。
'''


# 全局错误处理——>处理404
def error404(error):
    return render_template('error_404.html')
    # return error


# 全局错误处理——>处理500

def error500(error):
    return render_template('error_500.html')
    # return error


app.register_error_handler(500, error500)
app.register_error_handler(404, error404)

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
