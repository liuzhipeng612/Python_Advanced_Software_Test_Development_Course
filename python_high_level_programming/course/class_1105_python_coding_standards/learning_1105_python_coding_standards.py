# -*- coding: utf-8 -*-
"""
Python编码规范
"""


import requests
#
# # 什么是文档字符串
# # #模块，函数，类
# """
# 多行文本字符串
# """
# """单行文本字符串"""
# # 查看模块字符串
# print(requests.__doc__)
# # 查看方法的字符串
# print(requests.get.__doc__)
# print(requests.post.__doc__)
#
#
# # 封装公共的模块api的时候需要编写模块字符串，主要是告诉别人怎么使用这个模块，入参出参等
# def func2(name=None, age=None):
#     """自定义的函数
#
#     :param name: 名字
#     :param age: 年龄
#     :return:
#     """
#     return 666
#
#
# # 变量命名规范
# """
# 永远不要使用字母“i”“I”“O”作为单字符变量名
# """
# # 函数命名
# """
# 函数名应该小写，如果想提高可读性可以使用下划线分隔
# 大小写混合
# """


# 层级缩进
def long_function_name(
        par_one, par_two,
        par_three, par_four):
    return par_one, par_two, par_three, par_four


var_one = 1
var_two = 2
var_three = 3
var_four = 4

# 对齐缩进（左边括号对齐）
foo_one = long_function_name(var_one, var_two,
                             var_three, var_four)

# 悬挂缩进
foo_two = long_function_name(
    var_one, var_two,
    var_three, var_four)

# 没有使用垂直对齐时，禁止把参数放在第一行
foo_three = long_function_name(var_one, var_two,
    var_three, var_four)

# 当缩进没有与其他行区分时，要增加缩进
foo_four = long_function_name(
    var_one, var_two, var_three,
    var_four)
