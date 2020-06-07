#!/usr/bin/python3
# @FileName    :demo01_ajax.py
# @Time        :2020/6/7 下午12:47
# @Author      :ABC
# @Description :
import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024  # 通过设置配置项中的`MAX_CONTENT_LENGTH`参数限制上传文件的大小为1M，也就是1024*1024


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print('request.json:', request.json)
        return 'success!'


def allowed(filename):
    '''
    限制上传文件的类型
    '''
    support_file_extension_list = ['png', 'jpg', 'html', 'txt']
    file_extension = filename.split('.')[-1]
    if file_extension in support_file_extension_list:
        return True
    return False


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('pic')
    if file is None:
        return render_template('index.html')
    if allowed(file.filename):
        # secure_filename(filename)方法返回一个安全版本的文件名。它会将不规则(在浏览器URL里)的文件名重命名为规则的文件名。
        file.save(secure_filename(file.filename))
        print('file:', file)
        return 'save file success!'
    return 'error,unsupported file format!'


# 在浏览器中可以访问静态文件夹static中img目录下的图片
@app.route('/upload/<filename>', methods=['GET', 'POST'])
def get_upload(filename):
    # print('filename:', filename)
    # print('path1:', os.getcwd())
    # print('path2:', os.path.join(os.getcwd(), 'static/img'))
    return send_from_directory(os.path.join(os.getcwd(), 'static/img'), filename)


if __name__ == '__main__':
    app.run(debug=True)
