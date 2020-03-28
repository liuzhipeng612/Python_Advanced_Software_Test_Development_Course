import json

from django.http import Http404, JsonResponse
from django.views import View

from interfaces import serializers
from interfaces.models import Interfaces

"""
1.使用已学知识, 对Interface模型的增删改查接口进行优化

提示：
a.使用序列化器来实现反序列化(数据校验)和序列化过程(输出)	
b.使用序列化器来实现对数据的创建(create方法)和数据的更新(update方法)
c.把演练效果录屏上传(**推荐**)或者将效果截图上传或者上传代码文件(不要压缩)
"""


class InterfaceList(View):
    def post(self, request):
        """
        新增操作
        创建项目信息
        :param request:
        :return:
        """
        # 3.接收参数
        json_data = request.body  # 获取request中body的json格式数据
        # 4.反序列化输入
        python_data = json.loads(json_data, encoding="utr-8")
        # 5.校验输入数据
        serializer = serializers.InterfacesModelSerializer(data=python_data)  # 程序中的数据类型->序列化器
        try:
            serializer.is_valid(raise_exception=True)  # 开启校验失败后抛出异常
        except Exception:
            return JsonResponse(serializer.errors, status=400)  # 捕获异常并返回
        # 6.操作数据库
        serializer.save()  # 调用serializers的create方法进行创建数据
        # 7.序列化输出
        # 8.返回结果
        return JsonResponse(data=serializer.data)


class InterfaceDetail(View):
    """
    数据处理步骤：     # 根据输入和输出取舍对应步骤
    # 1.校验前端传递的pk值
    # 2.获取指定pk值的项目信息
    # 3.接收参数
    # 4.反序列化输入
    # 5.校验输入数据
    # 6.操作数据库
    # 7.序列化输出
    # 8.返回结果
    """

    # 1.校验前端传递的pk值
    def get_object(self, pk):
        try:
            return Interfaces.objects.get(id=pk)  # 查看数据库中是否存在该ID，如果有就返回该ID的模型类
        except Interfaces.DoesNotExist:
            raise Http404  # 如果数据库中不存在该ID，抛出Django默认的404页面

    def get(self, request, pk):
        """
        查询操作
        获取指定项目信息
        :param pk:
        :param request:
        :return:
        """
        # 2.获取指定pk值的项目信息
        one_interface = self.get_object(pk)
        # 7.序列化输出
        # 8.返回结果
        serializer = serializers.InterfacesModelSerializer(instance=one_interface)  # 程序中的数据类型->序列化器
        return JsonResponse(data=serializer.data)  # 序列化器对象调用data属性返回序列化格式数据json

    def put(self, request, pk):
        """
        修改操作
        更新指定的项目
        :param pk:
        :param request:
        :return:
        """
        # 2.获取指定pk值的项目信息
        one_interface = self.get_object(pk)
        # 3.接收参数
        json_data = request.body
        # 4.反序列化输入
        python_data = json.loads(json_data, encoding="utf-8")
        # 5.校验输入数据
        serializer = serializers.InterfacesModelSerializer(instance=one_interface, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(data=serializer.errors)
        # 6.操作数据库
        serializer.save()
        # 7.序列化输出
        # 8.返回结果
        return JsonResponse(data=serializer.data)

    def delete(self, request, pk):
        """
        删除操作
        删除指定的数据
        :param pk:
        :param request:
        :return:
        """
        # 2.获取指定pk值的项目信息
        one_interface = self.get_object(pk)
        # 6.操作数据库
        one_interface.delete()
        # 8.返回结果
        return JsonResponse(data={"messages": f"ID为{pk}的接口信息已删除"}, safe=False, status=204)
