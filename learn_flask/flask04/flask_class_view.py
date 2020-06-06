#!/usr/bin/python3
# @FileName    :flask_class_view.py
# @Time        :2020/6/6 下午5:40
# @Author      :ABC
# @Description : 可插拔视图代码示例
from flask import Flask, request
from flask.views import View

app = Flask(__name__)

# 统计某个url路由的访问次数
app.config['num'] = 0


# 记录页面访问次数的装饰器
def login_log(f):
    def decorator1(*args, **kwargs):
        app.config['num'] += 1
        return f(*args, **kwargs)  # 不要return其他的值，否则会被作为response返回

    return decorator1


# 可插拔视图，借鉴与Django的类视图
class ProjectView(View):
    def get(self):
        return "get-project"

    def post(self):
        return "post-project"

    # 分配请求
    def dispatch_request(self):
        dispatch_pattern = {'GET': self.get, "POST": self.post}
        method = request.method
        return dispatch_pattern.get(method)()


class CasesView(View):
    # 指定该类视图对应的视图函数可接收请求的方法
    methods = ['GET', 'POST']
    # 在类视图中显示使用装饰器方法二：使用decorators属性(定义在View类中，具体可以去查看View的源码)
    decorators = (login_log,)

    def get(self):
        return f"get-cases：这是你第{app.config.get('num')}次访问本页面!"

    def post(self):
        return f"post-cases：这是你第{app.config.get('num')}次访问本页面!"

    # 分配请求
    def dispatch_request(self):
        dispatch_pattern = {'GET': self.get, "POST": self.post}
        method = request.method
        return dispatch_pattern.get(method)()


# 在类视图中显示使用装饰器方法一：手动指定饰器
# f = login_log(CasesView.as_view('cases'))
# app.add_url_rule('/cases', view_func=f, methods=['GET', 'POST'])

# 注册路由
app.add_url_rule('/project', view_func=ProjectView.as_view('project'), methods=['GET', 'POST'])

f = CasesView.as_view('cases')
app.add_url_rule('/cases', view_func=f)

if __name__ == '__main__':
    app.run(debug=True)
