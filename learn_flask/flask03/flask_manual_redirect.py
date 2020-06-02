#!/usr/bin/python3
# @FileName    :flask_manual_redirect.py
# @Time        :2020/6/3 上午12:24
# @Author      :ABC
# @Description :
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return "这是home首页!"


print(app.url_map)


# @app.route("/login", methods=['GET'], endpoint='user_login', redirect_to='/')  # 在装饰器中设置重定向，程序运行时不会执行当前视图函数login()
# def login():
#     print('执行了login函数!')
#     return "登录成功!"

@app.route("/login", methods=['GET'], endpoint='user_login')
def login():
    print('执行了login函数!')
    return redirect('/')  # 需要从flask包中导入`redirect`方法


print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
