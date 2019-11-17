#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: 刘志鹏
@Contact: liuzhipeng612@gmail.com
@Project: Python_Advanced_Software_Test_Development_Course
@File: cw_1112_class_decorator.py
@Time: 2019/11/13 23:14
@Desc: Python Advanced Software Test Development Course
"""


# 第一题 ： 通过装饰器实现单例模式，只要任意一个类使用该装饰器装饰，那么就会变成一个单例模式的类。(面试真题)
class DecoratorClass:
    count = 0
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls.count == 0:
            cls._instance = super().__new__(cls)
            cls.count = 1
            return cls._instance
        else:
            return cls._instance

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print(F"我是类装饰器{self.__class__.__name__}新增功能1")
            res = func(*args, **kwargs)
            print(F"我是类装饰器{self.__class__.__name__}新增功能2")
            return res

        return wrapper


@DecoratorClass
class MyClass:

    def my1(self):
        return F"我是{__class__.__name__}的类方法{self.my1.__name__}"


myclass = MyClass()
print(id(myclass), myclass.my1())
myclassa2 = MyClass()
print(id(myclass), myclass.my1())

# 第二题：研究一个函数可不可以使用多个装饰器来装饰，如果可以请描述装饰器过程，如果不可以，请说出为什么（简答题）
