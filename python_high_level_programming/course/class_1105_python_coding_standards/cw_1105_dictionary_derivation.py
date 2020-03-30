#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: python_advanced_software_test_development
@File: cw_1105_dictionary_derivation.py
@Time: 2019/11/7 1:33
@Desc: Jungle old monster 
"""
"""
1、使用字典推倒是将下面字符串格式的数据，改成字典类型的数据
"""
cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28;sugstore=0;' \
           '__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'
cook_dict = {i.split("=")[0]: i.split("=")[1] for i in cook_str.split(";")}
"""
 2、定义一个函数实现以下功能，第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，
 不够50往后累加加到最后如果不够50也直接返回，因为没有可加的数据了
 
例子1 ：
a = [[1,3],[2,51],[3,49],[4,42],[5,42]] #入参 
a1 = [[2,54],[4,91],[5,42]] #返回 

例子2：
 b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参
 b1 = [[1,50],[4,57],[6,52]] #返回
"""

a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]    # 入参
a1 = [[2, 54], [4, 91], [5, 42]]    # 返回
"""
3、通过列表推导式完成下面数据类型转换
"""
li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
list_dict = [eval(i) for i in li1]
'''
4、通过列表推导式和字典推导式完成下面数据转换

# 转换后数据
list = [{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]
'''
str1 = """
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
"""
list_set = [i for i in str1.splitlines() if i]
dict_set = {i for list_set[i + 1] in list_set}
pass
