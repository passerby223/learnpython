#!/usr/bin/python3
# @FileName    :demo02_response.py
# @Time        :2020/6/9 下午10:53
# @Author      :ABC
# @Description : flaskz中的响应对象相关demo
import json

from flask import Flask, make_response, jsonify

app = Flask(__name__)
# 设置接口响应体不以ASCII格式展示，以中文展示。
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    # response_data = json.dumps({"username": "小花花"})
    # print('response_data:', response_data)
    # print('type(response_data):', type(response_data))

    # 手动构造一个响应头方法(1)：
    # return json.dumps({"username": "小花花"}), 203, {"content-type": "application/json"}

    # 手动构造一个响应头方法(2)：make_response()方法
    # response_data = make_response(json.dumps({"哈拉少儿": "哈撒给"}), {"content-type": "application/json"})
    # return response_data

    # 使用jsonify()方法自动将字典格式化为json格式，自动设置content-type=application/json
    response_data = jsonify({"name": "小花花", "age": 21, "gender": "女"})
    # 自定义响应状态码为207
    response_data.status = '207'
    return response_data


if __name__ == '__main__':
    app.run(debug=True)
