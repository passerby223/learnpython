#!/usr/bin/python3
# @FileName    :route_variable.py
# @Time        :2020/6/1 下午10:33
# @Author      :ABC
# @Description : flask路由动态参数代码示例
from flask import Flask, request
import uuid

print(uuid.uuid4())  # 4b994059-b244-44c8-ba7a-4282bb504f78
print(type(uuid.uuid4()))  # <class 'uuid.UUID'>

app = Flask(__name__)


@app.route("/param/<int:param>")
def param_int(param):
    return f"<h1>传入的int类型参数是：{param}，提示：传入其他类型参数会报错!</h1>"


@app.route("/param/<float:param>")
def param_float(param):
    return f"<h1>传入的float类型参数是：{param}，提示：传入其他类型参数会报错!</h1>"


@app.route("/param/<path:param>")
def param_path(param):
    return f"<h1>传入的path类型参数是：{param}，提示：传入其他类型参数会报错!</h1>"


@app.route("/param/<string:param>")
def param_string(param):
    return f"<h1>传入的string类型参数是：{param}，提示：传入其他类型参数会报错!</h1>"


@app.route("/hello")
def say_hello():
    name = request.args.get('name')
    age = request.args.get('age')
    return "<h1>hello " + name + ",你的年龄是" + age + "。</h1>"


if __name__ == '__main__':
    app.run(debug=True)