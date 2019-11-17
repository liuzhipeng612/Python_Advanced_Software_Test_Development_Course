#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: 刘志鹏
@Contact: liuzhipeng612@gmail.com
@Project: Python_Advanced_Software_Test_Development_Course
@File: leaning.py
@Time: 2019/11/17 23:49
@Desc: Python Advanced Software Test Development Course
"""


class Decorator(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("装饰器扩展的新功能一")
        res = self._func(*args, **kwargs)
        print("装饰器扩展的新功能2")
        return res


@Decorator
def func():
    print("func这个功能函数的代码")


func()
