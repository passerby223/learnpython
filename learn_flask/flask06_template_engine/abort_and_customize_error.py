# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/6/11 下午10:32
# @Author    : ABC
# @FileName  : abort_and_customize_error.py

from flask import Flask, render_template, abort, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

'''
自定义响应错误方法(一)：使用abort()方法
'''


@app.errorhandler(401)
def error401(error):
    return render_template('error_401.html'), 401


@app.route('/')
def index():
    if not request.args.get('user'):
        # 通过abort()函数来自定义响应错误
        abort(401)
    return 'index'


'''
自定义响应错误方法(二)：自定义异常，并继承自Exception类，然后使用装饰器@app.errorhandler(自定义异常类的类名)来装饰表示错误的函数，比如下边的：
@app.errorhandler(ProjectNotFoundError)
def error404(error):
    return render_template('error_404.html'), 404
'''


class ProjectNotFoundError(Exception):
    pass


@app.errorhandler(ProjectNotFoundError)
def error404(error):
    return render_template('error_404.html'), 404


@app.route('/project')
def project():
    if not request.args.get('projectId'):
        raise ProjectNotFoundError()
    return f"projectId is {request.args.get('projectId')}"


'''
自定义响应错误方法并返回json格式的数据,适用于前后端分离项目
'''


class CaseNotFoundError(Exception):
    pass


@app.errorhandler(CaseNotFoundError)
def error_case_404(error):
    return jsonify({'code': -1, 'msg': '未找到相关资源'}), 404


@app.route('/cases')
def case():
    if not request.args.get('caseId'):
        raise CaseNotFoundError()

    return jsonify({'code': 0, 'msg': 'success', 'caseId': request.args.get('caseId')}), 200


if __name__ == '__main__':
    app.run(debug=True)
