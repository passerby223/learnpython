'''
-*- coding: utf-8 -*-
@Author  : ABC
@Time    : 2019/10/15 23:57
@Software: PyCharm
@File    : subprocess_test.py
'''
import subprocess as sp


class TestSubprocess:
    # /root/wenbin/sug.log
    def read_files(self, file_path):
        content = sp.Popen('cat ' + file_path, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        return {'stdout': content.stdout.read().decode('utf-8'), 'stderr': content.stderr.read().decode('utf-8')}


if __name__ == '__main__':
    test = TestSubprocess()
    file_path = '/root/wenbin/sug.log'
    print(test.read_files(file_path))