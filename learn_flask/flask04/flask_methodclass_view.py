#!/usr/bin/python3
# @FileName    :flask_methodclass_view.py
# @Time        :2020/6/6 下午7:44
# @Author      :ABC
# @Description :

from flask import Flask
from flask.views import MethodView

app = Flask(__name__)

# 统计某个url路由的访问次数
app.config['num'] = 0


# 记录页面访问次数的装饰器
def login_log(f):
    def decorator1(*args, **kwargs):
        app.config['num'] += 1
        return f(*args, **kwargs)  # 不要return其他的值，否则会被作为response返回

    return decorator1


class ProjectView(MethodView):
    # 继承MethodView类后，可以不指定methods属性了，程序会自动根据getattr()获取请求的method后去调用对应的方法。
    decorators = (login_log,)

    def get(self):
        return f"get-cases：这是你第{app.config.get('num')}次访问本页面!"

    def post(self):
        return f"post-cases：这是你第{app.config.get('num')}次访问本页面!"

    def put(self):
        return f"put-cases：这是你第{app.config.get('num')}次访问本页面!"

    def delete(self):
        return f"delete-cases：这是你第{app.config.get('num')}次访问本页面!"


app.add_url_rule('/project', view_func=ProjectView.as_view('project'))

if __name__ == '__main__':
    app.run()
