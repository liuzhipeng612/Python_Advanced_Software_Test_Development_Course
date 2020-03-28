#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: 刘志鹏
@Contact: liuzhipeng612@gmail.com
@Project: Python_Advanced_Software_Test_Development_Course
@File: danlihanshu.py
@Time: 2019/11/18 0:05
@Desc: Python Advanced Software Test Development Course
"""


class MyClass(object):
    count = 0
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.count == 0:
    #         cls._instance = super().__new__(cls)
    #         cls.count = 1
    #         return cls._instance
    #     else:
    #         return cls._instance
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))
