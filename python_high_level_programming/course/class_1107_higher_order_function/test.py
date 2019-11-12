class MyClass(object):
    def func(self):  # 普通实例方法
        print("这是func----------")

    @classmethod
    def func2(cls):  # 这个是类方法
        print("这是func2-----------")

    @staticmethod
    def func3():  # 这个是静态方法
        print("这是func3---------")

    @property
    def func1(self):  # 这个方法可以像属性一样被访问
        print("这是func1------------")
