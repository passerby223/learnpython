# Flask
## 简单介绍
* `Flask`是一个使用`Python`编写的`轻量级Web应用框架`。其`WSGI工具箱`采用`Werkzeug`，`模板引擎`则使用`Jinja2`。`Flask`使用`BSD授权`。
* Flask也被称为`microframework`，因为它使用简单的核心，用`extension`增加其他功能。`Flask`没有默认使用的`数据库`、`窗体验证工具`。
## 通过pip安装flask
```bash
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
```
## 编写第一个flask程序
```python
#!/usr/bin/python3
# @FileName    :first_flask_script.py
# @Time        :2020/5/31 上午12:45
# @Author      :ABC
# @Description :第一个flask程序

# 从flask包导入需要用到的包
from flask import Flask, render_template, request

# 初始化application
app = Flask(__name__)


# 添加路由
@app.route("/")
def index():
    # args = request.args # 获取传入的的参数 可以是：params形式参数、form形式参数、json形式参数、file格式文件
    data = request.args.get("user")

    if data is None:
        return "<h1 style='color:red'>这是index界面</h1>"
    else:
        return "<h1 style='color:red'>hello!" + data + ", 欢迎来到index界面!</h1>"


@app.route("/hello")
def hello():
    # 返回一个HTML格式的文件(默认所有HTML文件都存储在templates目录下，当访问程序运行时匹配到`/hello`时，会自动去templates目录下查找匹配到的HTML文件)
    return render_template('hello.html')


# 运行服务器
# 也可以通过关键字参数绑定host、port、debug(是否开启debug模式：True/False 开启后再更改完代码后，会自动重启flask应用)
app.run(port=12306, debug=True)
```
templates目录下的hello.html文件
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>自我介绍</title>
</head>
<body>
<h1>个人信息介绍</h1>
<p>你好，我是小花花</p>
<p>我今年21岁，喜欢打乒乓球，旅游</p>
</body>
</html>
```
## 程序执行效果
### 访问根路径`/`不传参数
![根路径](根路径.png)
### 访问根路径`/`带参数
![根路径带参数](根路径带参数.png)
### 访问路径`/hello`返回一个HTML页面
![返回HTML页面](路径hello.png)

好了，以上今天分享的第一个flask小程序的全部内容了。接下来会持续更新~

# Flask设置配置项、视图函数绑定多路由及自定义装饰器的使用
## Flask设置配置项
可以通过`app.config['key值'] = value值`来修改以下默认配置参数
```python
default_config = ImmutableDict(
        {
            "ENV": None,
            "DEBUG": None,
            "TESTING": False,
            "PROPAGATE_EXCEPTIONS": None,
            "PRESERVE_CONTEXT_ON_EXCEPTION": None,
            "SECRET_KEY": None,
            "PERMANENT_SESSION_LIFETIME": timedelta(days=31),
            "USE_X_SENDFILE": False,
            "SERVER_NAME": None,
            "APPLICATION_ROOT": "/",
            "SESSION_COOKIE_NAME": "session",
            "SESSION_COOKIE_DOMAIN": None,
            "SESSION_COOKIE_PATH": None,
            "SESSION_COOKIE_HTTPONLY": True,
            "SESSION_COOKIE_SECURE": False,
            "SESSION_COOKIE_SAMESITE": None,
            "SESSION_REFRESH_EACH_REQUEST": True,
            "MAX_CONTENT_LENGTH": None,
            "SEND_FILE_MAX_AGE_DEFAULT": timedelta(hours=12),
            "TRAP_BAD_REQUEST_ERRORS": None,
            "TRAP_HTTP_EXCEPTIONS": False,
            "EXPLAIN_TEMPLATE_LOADING": False,
            "PREFERRED_URL_SCHEME": "http",
            "JSON_AS_ASCII": True,
            "JSON_SORT_KEYS": True,
            "JSONIFY_PRETTYPRINT_REGULAR": False,
            "JSONIFY_MIMETYPE": "application/json",
            "TEMPLATES_AUTO_RELOAD": None,
            "MAX_COOKIE_SIZE": 4093,
        }
    )
```
比如设置当前application运行环境为开发环境(默认是生产环境)
```python
# 设置配置项
# 设置开启debug模式
app.config['DEBUG'] = True
# 设置启用服务器的端口
app.config['PORT'] = 12306
# 设置application的当前运行环境为开发环境,默认不设置的时候为生产环境
app.config['ENV'] = 'development'
```
未设置application的当前运行环境为`开发环境`前，启动服务控制台输出如下
```bash
* Running on http://127.0.0.1:12306/ (Press CTRL+C to quit)
* Restarting with stat
* Serving Flask app "flask02" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Debugger is active!
* Debugger PIN: 740-975-992
```
设置application的当前运行环境为`开发环境`后，启动服务控制台输出如下
```bash
* Running on http://127.0.0.1:12306/ (Press CTRL+C to quit)
* Restarting with stat
* Serving Flask app "flask02" (lazy loading)
* Environment: development
* Debug mode: on
* Debugger is active!
* Debugger PIN: 740-975-992
```
对比一下上边的两次控制台输出，可以看出使用默认`生产环境`开运行flask服务时，会提示：`这是一个开发服务器。不要在生产部署中使用它。请改用生产WSGI服务器。`

相对于flask，生产服务器可以选用**uWSGI**或**Nginx**
* uWSGI：uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。
    * WSGI / uwsgi / uWSGI 这三个概念的区分
        * WSGI是一种通信协议。Web服务器网关接口(Python Web Server Gateway Interface，缩写为WSGI)是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
        * uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
        * 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。
* Nginx：Nginx(engine x)是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。
    * Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。
## Flask视图函数绑定多路由
有时候我们需要设置访问`多个url路径`返回的`页面数据`或`后端处理逻辑`都一致，这时候就可以通过`视图函数绑定多路由`来实现。

示例
```python
@app.route("/index")
@app.route("/helloWorld")
@app.route("/")
def index():
    return "helloWorld"
```
此时运行flask服务，分别访问`http://127.0.0.1:12306/`, `http://127.0.0.1:12306/index`, `http://127.0.0.1:12306/helloWorld`, 前端页面展示的效果都相同，都是`helloWorld`
## 自定义装饰器的使用
有时候我们需要统计某个URL路由的访问次数，就可以通过设置自定义装饰器来实现。

示例
```python
#!/usr/bin/python3
# @FileName    :flask02.py
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


# 打印当前时间的装饰器
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
```
然后启用flask服务，前端访问`http://127.0.0.1:12306/hello` 多次，每访问一次，`app.config['num']`就加1，然后前端页面返回本次是第n次访问本页面。

效果如下

第一次访问`http://127.0.0.1:12306/hello` 

![hello01](hello01.png)

刷新当前页面

![hello02](hello02.png)

再次刷新当前页面

![hello03](hello03.png)

以此类推，没刷新一次页面访问页面次数就加1。

好啦，以上就是今天分享的全部内容了，其实学web开发挺有意思的(手动吃瓜~)
