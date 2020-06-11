#!/usr/bin/python3
# @FileName    :flask02_decorator_and_env.py
# @Time        :2020/5/31 下午9:55
# @Author      :ABC
# @Description :
import time
from flask import Flask

app = Flask(__name__)


# 打印当前时间的装饰器
def log_time(f):
    def decorator(*args, **kwargs):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return f(*args, **kwargs)  # 不要return其他的值，否则会被作为response返回

    return decorator


# 记录页面访问次数的装饰器
def log_time1(f):
    def decorator1(*args, **kwargs):
        app.config['num'] += 1
        return f(*args, **kwargs)  # 不要return其他的值，否则会被作为response返回

    return decorator1


# 一个视图函数上可以同时绑定多个url路由规则
# 如果还有其它装饰器该怎么处理？
# 1.视图装饰器应该放在最外层(比如下边的`@log_time`)，否则里边的装饰器不会生效 2.视图函数包裹的装饰器不要return新值，否则会被包装成返回数据返回
# 常用视图函数来统计某个url路由的访问量或记录时间日志
@app.route("/index")
@app.route("/helloWorld")
@app.route("/")
@log_time
def index():
    return "helloWorld"


@app.route("/hello")
@log_time1
def index():
    return "你好，我叫小花花!这是你第{}次访问本页面!".format(app.config.get('num'))


# 设置配置项
# 设置开启debug模式
app.config['DEBUG'] = True
# 设置启用服务器的端口
app.config['PORT'] = 12306
# 设置application的环境为开发环境,默认不设置的时候为生产环境
app.config['ENV'] = 'development'
# 统计某个url路由的访问次数
app.config['num'] = 0

if __name__ == '__main__':
    app.run(port=app.config.get('PORT'), debug=app.config.get('DEBUG'))
