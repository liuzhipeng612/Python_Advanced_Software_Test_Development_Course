#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
==============================
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: course
@File: test.py
@Time: 2019/11/11 22:42
@Desc: Jungle old monster 
==============================
"""


def funcB1():
    print("这个是函数funcB1")

    def funcB2():
        print("这个是函数funcB2")

    return funcB2


fu = funcB1()
print(fu)
# fu()





