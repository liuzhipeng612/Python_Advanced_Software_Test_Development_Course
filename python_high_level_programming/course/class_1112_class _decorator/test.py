#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: 刘志鹏
@Contact: liuzhipeng612@gmail.com
@Project: Python_Advanced_Software_Test_Development_Course
@File: test.py
@Time: 2019/11/14 0:35
@Desc: Python Advanced Software Test Development Course
"""


def f1(func):
    def fun(*args, **kwargs):
        print("------执行装饰器实现的功能-------")
        return func(*args, **kwargs)

    return fun


@f1
class Hero(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("正在初始化")

    def move(self):
        print("%s在快速移动" % self.name)


laoli = Hero("老李", 19)
print(laoli.name)

# 调用装饰器，将下方函数或类作为参数传到装饰器，装饰器会执行新函数方法和原函数方法或类返回给原函数方法或类
