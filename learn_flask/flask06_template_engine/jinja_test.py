# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/13 下午2:37
# @Author    : ABC
# @FileName  : jinja_test.py

from flask import Flask, jsonify, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
