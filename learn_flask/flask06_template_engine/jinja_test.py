# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/13 下午2:37
# @Author    : ABC
# @FileName  : jinja_test.py

from flask import Flask, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)
'''
密钥用于会话cookie的安全签名，并可用于应用或者扩展的其他安全需求。本变量应当是一个字节型长随机字符串，虽然unicode也是可以接受的。
如果在使用flask中的session时，不添加`app.config['SECRET_KEY'] = 'dsklnbvkldnvk'`这一项，将会报以下错误：
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
'''
app.config['SECRET_KEY'] = 'dsklnbvkldnvk'


@app.route('/')
def student_list():
    # 构造虚拟数据
    students = [
        {"name": "小花", "age": 21, "gender": "女"},
        {"name": "小明", "age": 34, "gender": "男"},
        {"name": "小张", "age": 12, "gender": "男"},
        {"name": "小二", "age": 25, "gender": "女"}
    ]
    # 返回一个HTML文件，并制定上下文参数，可以在HTML文件中接收这些参数，然后拿到数据使用jinja2模板引擎进行数据渲染
    return render_template('student_list.html', student_list=students, title='学生信息列表')


print(app.url_map)


@app.route('/login/<username>')
def login(username):
    # session(一个全局变量),可用于记住登录用户名。需要从flask包导入。
    session['user'] = username
    return redirect(url_for('student_list'))


if __name__ == '__main__':
    app.run(debug=True)
