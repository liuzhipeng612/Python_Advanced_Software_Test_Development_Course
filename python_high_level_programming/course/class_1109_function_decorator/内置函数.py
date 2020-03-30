"""
内置函数
- locals函数：获取当前作用域所有的变量，打包字典
- globlas函数：获取全局作用域所有的变量，打包字典
- map函数：将函数应用于iterable中每一项并输出期结果的迭代器
- filter函数：过滤器
- zip函数：聚合打包
"""
# --------------
# aa = 100
# bb = 200
#
# dic1 = locals()
# print(dic1)
# --------------
# def func():  # 一般用在函数内部，获取函数的作用域所有变量
#     aa = 100
#     bb = 200
#
#     dic1 = locals()
#     print(dic1)
#
#
# func()
# --------------
# def func1(c):
#     aa = 100
#     bb = 200
#
#     dic1 = locals()
#     print(dic1)
#
#
# func1(999)
# --------------
# dic = globals()
# print(dic)
# --------------
# if "name" in globals():
#     print("全局变量中已经有name这个变量了")
# else:
#     name = "python666"
#     print("重新设置全局变量为name=python666")
# --------------
# name = "python999"
# if "name" in globals():
#     print("全局变量中已经有name这个变量了")
# else:
#     name = "python666"
#     print("重新设置全局变量为name=python666")
# --------------
# map 自动遍历可迭代对象，将可迭代对象中的每一个元素当做参数传到函数中
"""
参数一：函数
参数二：可迭代对象
学习笔记：使用匿名函数作为map参数，自动遍历匿名函数列表中的元素，作为参数传入匿名函数的变量中作为参数，
将匿名函数的值放入map对象中，即新的列表中。
"""
# res = map(lambda x: x * 2, [11, 22, 33, 44, 55])
# print(res)
# --------------
# res = map(lambda x: x * 2, [11, 22, 33, 44, 55])
# print(list(res))  # 将map对象转换成列表
# --------------
# res = map(lambda x, y: x + y, [11, 22, 33, 44, 55], [111, 222, 333, 444, 555])
# print(list(res))
# --------------
# import openpyxl
#
# wb = openpyxl.load_workbook("common.xlsx")
# sh = wb["register"]
# # print(list(sh.rows))
# r = list(sh.rows)[1]  # 返回的是一个对象
# print(r)
# res = map(lambda x: x.value, r)  # 将对象中的值提取出来
# print(list(res))

# --------------
# filter函数 自动遍历可迭代对象，将可迭代对象中的每一个元素当做参数传到函数中
"""
参数一：函数
参数二：可迭代对象
老师笔记：自动遍历第二个参数，把每个元素当成参数，传到一个参数（函数），根据函数返回值是True还是false来进行过滤
学习笔记：使用匿名函数作为filter参数，自动遍历匿名函数列表中的元素，作为参数传入匿名函数的变量中作为参数，
根据匿名函数返回的值是True还是False来过滤，将过滤出来的值放入filter对象中，即新的列表中。

值为True的会被放入filter对象中，值为False的会被遗弃
"""
# li = [11, 22, 33, 44, 55]
# res = filter(lambda x: x > 33, li)
# print(list(res))
# --------------
# zip函数：聚合打包
"""
主要使用两组数据进行聚合比较多，多组聚合使用场景较少
zip函数只能使用一次，再次调用需要再次执行
zip函数可以使用dict()直接转换成字典类型的数据
zip函数可以使用list()直接转换成列表，但是列表对象是元组
"""
# title = ["a", "b", "c", "d"]
# data = [11, 22, 33]
#
# res3 = zip(title, data)
# print(list(res3))
# --------------
# title = ["a", "b", "c", "d"]
# data1 = [1, 2, 3]
# data2 = [11, 22, 33]
# data3 = [111, 222, 333]
# data4 = [1111, 2222, 3333]
#
# res3 = zip(title, data1, data2, data3, data4)
# print(list(res3))
# --------------
title = ["a", "b", "c", "d"]
data1 = [1, 2, 3]

res3 = zip(title, data1)
print(dict(res3))
