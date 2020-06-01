#!/usr/bin/python3
# @FileName    :flask_redirect.py
# @Time        :2020/6/1 下午11:47
# @Author      :ABC
# @Description :
from flask import Flask

app = Flask(__name__)


# @app.route("/index")
# def index1():
#     return "这是index页面!"

@app.route("/index/")
def index():
    return "这是index页面!"


if __name__ == '__main__':
    app.run(debug=True)
