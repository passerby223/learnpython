#!/usr/bin/python3
# @FileName    :flask_request.py
# @Time        :2020/6/6 下午11:21
# @Author      :ABC
# @Description :flask中的request详解
from flask import Flask, request, Request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    a = request
    print('a--->', a)
    # 获取get请求的字符串形式的入参(?key1=value1&key2=value2)
    get_params = request.args
    print("get_params--->", get_params) # get_params---> ImmutableMultiDict([('get_name', '小花花')])
    # 获取post请求的form形式的入参
    post_form_params = request.form
    print("post_form_params--->", post_form_params) # post_form_params---> ImmutableMultiDict([('form_name', '熊大')])
    # 获取post请求的json形式的入参
    post_json_params = request.json
    print("post_json_params--->", post_json_params) # post_json_params---> {'name': '熊二'}
    # 获取file文件形式的参数
    file_params = request.files
    print("file_params--->", file_params)
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
