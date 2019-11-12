#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
==============================
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: course
@File: cw_1109_function_decorator.py
@Time: 2019/11/11 22:31
@Desc: Jungle old monster 
==============================
"""
import time


# 1、请设计一个装饰器，接收一个int类型的参数number，可以用来装饰任何的函数， 如果函数运行的时间大于number，则打印出函数名和函数的运行时间


def funcA2(func):
    def funcA3(number):
        start_time = time.time()
        func()
        end_time = time.time()
        run_time = end_time - start_time
        if run_time > number:
            print(F"函数{func.__name__}的运行时间为{run_time}")

    return funcA3


@funcA2
def funcA1():
    s = 0
    for i in range(100000000):
        s += i
    print(s)


funcA1(5)


# 2、 请设计一个装饰器  ，可以给函数扩展登录认证的功能（提示数账号密码，然后进行校验），多个函数同时使用这个装饰器， 调用函数的时候，
# 只要登录成功一次，后续的函数无需再进行登录（默认的认证账号：qwe123，密码：123456）
def funcB6(func):
    def funcB7():
        print("xxx")

    return funcB7


@funcB6
def funcB1():
    pass


@funcB6
def funcB2():
    pass


@funcB6
def funcB3():
    pass


@funcB6
def funcB4():
    pass


@funcB6
def funcB5():
    pass


funcB1()
funcB2()
funcB3()
funcB4()
funcB5()
