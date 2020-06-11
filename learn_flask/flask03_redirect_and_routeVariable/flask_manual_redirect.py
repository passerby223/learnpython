#!/usr/bin/python3
# @FileName    :flask_manual_redirect.py
# @Time        :2020/6/3 上午12:24
# @Author      :ABC
# @Description :
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/", endpoint='home')
def home():
    return "这是home首页!"


print(app.url_map)


# 路由重定向方法1
# @app.route("/login", methods=['GET'], endpoint='user_login', redirect_to='/')  # 在装饰器中设置重定向，程序运行时不会执行当前视图函数login()
# def login():
#     print('执行了login函数!')
#     return "登录成功!"

# 路由重定向方法2
@app.route("/login", methods=['GET'], endpoint='user_login')
def login():
    print('执行了login函数!')
    # endpoint代表视图函数和路由的绑定关系。
    # 使用url_for(endpoint=xxx)方法配合redirect()进行路由重定向操作。
    '''
    为什么要使用url_for(endpoint=xxx)方法？
    因为通常我们路由的地址会因为需求而经常改变，但是endpoint(视图函数和路由的绑定关系)是固定的，
    所以可以通过url_for(endpoint=xxx)方法再配合redirect()进行路由重定向操作。
    '''
    return redirect(url_for(endpoint='.home'))  # 需要从flask包中导入`redirect`方法


@app.route("/project/<int:id>", methods=['GET'], endpoint='project')
def project(id):
    print('执行了project函数!')
    return redirect(url_for(endpoint='.project_detail', project_id=id, username='hah'))  # 需要从flask包中导入`redirect`方法


# 路由重定向:url_for()带关键字参数 **很重要**
@app.route("/project_detail", methods=['GET'], endpoint='project_detail')
def project_detail():
    print('执行了project_detail函数!')
    return f"current function is project_detail, and project_id = {request.args.get('project_id')}, " \
           f"username = {request.args.get('username')}"


'''
url_for生成静态文件,**很重要**
url_for('static', filename='test.css')
'''

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
