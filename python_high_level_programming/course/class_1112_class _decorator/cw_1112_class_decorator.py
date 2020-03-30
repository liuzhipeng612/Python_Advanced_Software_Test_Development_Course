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
    def __init__(self, obj):  # 如果采用闭包函数类型作为类函数，将被装饰类的函数func作为装饰器__init__的参数，执行被装饰类的时候，该类的函数会变为类装饰器的属性
        self._obj = obj

    def __call__(self, *args, **kwargs):
        print(F"我是类装饰器{self.__class__.__name__}新增功能1")
        self._obj(*args, **kwargs)
        print(F"我是类装饰器{self.__class__.__name__}新增功能2")
"""
instantiate=DecoratorClass()

"""

@DecoratorClass
class MyClassA1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def my1(self):
    #     return F"我是{__class__.__name__}的类方法{self.my1.__name__}"


myclassa1 = MyClassA1("刀刀", "18")
print(id(myclassa1), myclassa1.name)
# print(id(myclassa1), myclassa1.my1())

# 第二题：研究一个函数可不可以使用多个装饰器来装饰，如果可以请描述装饰器过程，如果不可以，请说出为什么（简答题）
