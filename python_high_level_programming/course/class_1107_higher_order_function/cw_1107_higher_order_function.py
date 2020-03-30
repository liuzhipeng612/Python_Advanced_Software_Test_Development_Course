#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 一、一个球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
1      2            3           4              5
初始值  回弹值 初始值  回弹值
100    50-----50    25-----25    12.5-----12.5    6.25-----6.25    3.125
"""


# 求当前反弹的高度
def funcA1(n):
    a = 100
    if n == 1:
        b = a / 2
        return b
    else:
        return funcA1(n - 1) / 2


func_a1 = funcA1(5)
print(F"第十次反弹的高度：{func_a1}")


# 求总共经过多少米
def funcA2(n):
    a = 100
    if n == 1:
        b = a + a / 2
        return b
    else:
        return funcA2(n - 1) + funcA2(n - 1) / 2


func_a2 = funcA2(2)
print(F"第十次反弹总共经过米数为：{func_a2}")

# 二、古典问题：有一对兔子，第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# （意味着生长期为2个月） （递归实现）
"""
只数 -   1   2   3   4   5   6   7   8   9   10  11  12  13
月份 对数 兔子：月份
1   1
2   1
3   2   1:3 1:1
4   3   1:4 1:2 1：1
5   5   1:5 1:3 1:2 1:1 1:1   
6   8   1:6 1:4 1:3 1:2 1:2 1:1 1:1 1:1
7   13  1:7 1:5 1:4 1:3 1:3 1:2 1:2 1:2 1:1 1:1 1:1 1:1 1:1
"""


def funcB1(n):
    if n < 3:
        return 1 * 2
    else:
        first_two = funcB1(n - 1)
        first_one = funcB1(n - 2)
        return first_two + first_one


func_b1 = funcB1(7)
print(F"第七个月总共有{func_b1}个兔子")

# 三、小明有100元钱 打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共有多少种买法?（面试笔试题）
"""
有100块钱 A本数*5+B本数*3+C本数*1 >=100
"""


def funcC1(n):
    count = 0
    for a in range(n // 5 + 1):
        for b in range(n // 3 + 1):
            c = 100 - a - b
            if a * 5 + b * 3 + c * 0.5 >= n:
                count += 1
    return count


func_c1 = funcC1(100)
print(F"100元钱有{func_c1}种买法")
