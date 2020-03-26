# coding: utf-8 
# @Time    : 2020/3/14 下午8:37
# @File    : paramiko_practice.py
# @Software: PyCharm

import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def _ssh_login(ip, username, password):
    '''
    ssh 登录服务器
    :param ip:服务器IP
    :param username: 登录服务器的账号
    :param password: 登录服务器的密码
    :return:
    '''
    ssh.connect(ip, 22, username, password)


def select_content(select_str, file_name):
    '''
    查看文件中某个字符串所在行及所在行的内容
    :param select_str: 输入查询的字符串
    :param file_name: 输入查询的字符串所在的文件的绝对路径
    :return: stdout：标准输出 stderr：标准错误输出
    '''
    stdin, stdout, stderr = ssh.exec_command(
        "sed -n -e '/" + select_str + "/p' -e '/" + select_str + "/='  " + file_name)
    stdout_content = stdout.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    stderr_content = stderr.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    return stdout_content, stderr_content


def change_content(old_str, new_str, line_number, file_name):
    '''
    修改文件中某一行的字符串
    :param old_str:输入需要替换的原始字符串
    :param new_str: 输入需要替换的新字符串
    :param line_number: 输入需要替换的原始字符串所在行号
    :param file_name: 输入需要替换的原始字符串所在文件的绝对路径
    :return: stdout：标准输出 stderr：标准错误输出
    '''
    stdin, stdout, stderr = ssh.exec_command(
        "sed -i '" + line_number + "s/" + old_str + "/" + new_str + "/' " + file_name)
    stdout_content = stdout.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    stderr_content = stderr.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    return stdout_content, stderr_content


def select_content_with_line_number(line_number):
    '''
    查看字符串所在行的所有内容
    :param line_number: 修改操作完成后,打印被修改行的所有内容，确认是否修改已生效
    :return: stdout：标准输出 stderr：标准错误输出
    '''
    stdin, stdout, stderr = ssh.exec_command(
        "sed -n '" + line_number + "p' " + file_name)
    stdout_content = stdout.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    stderr_content = stderr.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    return stdout_content, stderr_content


def view_all_contents_of_a_file(filename):
    '''
    查看文件所有内容并显示行号
    :param filename: 被查看所有内容的文件
    :param line_number: 修改操作完成后,打印被修改行的所有内容，确认是否修改已生效
    :return: stdout：标准输出 stderr：标准错误输出
    '''
    stdin, stdout, stderr = ssh.exec_command("cat -n " + filename)
    stdout_content = stdout.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    stderr_content = stderr.read().decode('utf-8')  # 以utf-8编码对结果进行解码
    return stdout_content, stderr_content


if __name__ == '__main__':
    # 程序的入口
    while 1:
        user_input = input('请输入远程服务器的IP,用户名,密码分别以空格隔开(示例：127.0.0.1 root 123456)>>>')
        if len(user_input.split(' ')) == 3:
            ip = user_input.split(' ')[0]
            user_name = user_input.split(' ')[1]
            pass_word = user_input.split(' ')[2]
            _ssh_login(ip, user_name, pass_word)
            while 1:
                print('一条靓丽的分割线'.center(100, '*'))
                user_choice1 = input('请输入序号选择任务\n0 退出程序\n1 操作文件\n>>>')
                if user_choice1 == '0':
                    ssh.close()
                    sys.exit()
                elif user_choice1 == '1':
                    print('一条靓丽的分割线'.center(100, '*'))
                    file_name = input('请输入需要操作的文件名(输入被操作文件在服务器中的绝对路径!)>>>')
                    while 1:
                        print('一条靓丽的分割线'.center(100, '*'))
                        user_choice2 = input('请输入序号选择任务\n0 退出程序\n1 重新选择文件\n'
                                             '2 查询文件中的某个字符串所在行的内容及行号\n3 修改文件中的某个字符串\n4 查看文件中所有内容\n>>>')
                        if user_choice2 == '0':
                            ssh.close()
                            sys.exit()
                        elif user_choice2 == '1':
                            break
                        elif user_choice2 == '2':
                            select_string = input('请输入需要查询的字符串>>>')
                            str_raw_select = select_content(select_string, file_name)
                            if str_raw_select[0] != '':
                                print("{}文件中查询到包含有'{}'字符串的行的所有内容及行号如下>>>".format(file_name, select_string))
                                print(str_raw_select[0])
                            elif str_raw_select[0] == '' and str_raw_select[1] == '':
                                print("'{}'字符串在{}文件中不存在哦!请重新输入字符串".format(select_string, file_name))
                            elif str_raw_select[1] != '':
                                print("{}文件不存在哦!请检查文件绝对路径是否正确!,详细报错信息如下>>>".format(file_name))
                                print(str_raw_select[1])
                            else:
                                print(str_raw_select)
                                print('啊哦~发生了未知错误!请重新运行程序!')
                        elif user_choice2 == '3':
                            print('以下三项都为必输入项!')
                            change_string_old = input('请输入需要修改的字符串>>>')
                            change_string_new = input('请输入新的字符串>>>')
                            change_string_line_number = input('请输入该字符串所在行号>>>')
                            if change_string_line_number != '' and change_string_old != '' and change_string_new != '':
                                try:
                                    change_res = change_content(change_string_old, change_string_new,
                                                                change_string_line_number, file_name)
                                    if change_res[1] != '':
                                        print('{}文件不存在或输入有误!详细报错信息如下>>>\n{}'.format(file_name, change_res[1]))
                                    else:
                                        print('修改已完成!修改后第{}行的内容为(请务必根据以下输出自行核验修改是否成功!)>>>'.format(
                                            change_string_line_number))
                                        select_line_num_res = select_content_with_line_number(change_string_line_number)
                                        print(select_line_num_res[0])
                                except Exception as err:
                                    print('本次修改操作报错了,报错信息如下：{}'.format(err))
                            else:
                                print('输入有误!旧字符串、新字符串及行号为必输入项!')
                        elif user_choice2 == '4':
                            file_all_content_raw = view_all_contents_of_a_file(file_name)
                            if file_all_content_raw[0] != '':
                                print('{}文件中的所有内容为>>>'.format(file_name))
                                print(file_all_content_raw[0])
                            elif file_all_content_raw[1] != '':
                                print('{}文件不存在或文件绝对路径错误,请输入1重新选择文件,详细报错信息如下>>>'.format(file_name))
                                print(file_all_content_raw[1])
                            else:
                                print('啊哦~发生了未知错误!请重新运行程序!')
                        else:
                            print('输入有误!请重新输入!')
                else:
                    print('输入有误!请重新输入!')
        else:
            print('输入有误!请重新输入!')

