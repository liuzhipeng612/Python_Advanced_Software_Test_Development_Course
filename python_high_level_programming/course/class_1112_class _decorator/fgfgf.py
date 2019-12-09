# 类中没有实现__call__方法：
# class A:  # 类中没有实现__call__方法
#     pass
#
#
# a = A()
# a()  # 类对象不可调用


# 类中实现了__call__方法：
class B:
    def __init__(self):
        self.name = 'zhangsan'

    def __call__(self):  # 类中实现了__call__方法
        print('类中实现了__call__方法：', self.name)


b = B()
b()  # 类对象可调用，并在调用类对象的时候，自动执行__call__方法
