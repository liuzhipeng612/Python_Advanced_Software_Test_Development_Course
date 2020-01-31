import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View

from interfaces.models import Interfaces
from projects.models import Projects
from . import serializers


class ProjectList(View):
    def get(self, request):
        """

        :param request:
        :return:
        """
        # 1、从数据库中获取所有项目的信息
        project_qs = Projects.objects.all()
        # 2、将模型类对象转化为字典类型，构造嵌套字典的列表-反序列化
        serializer = serializers.ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    def post(self, request):
        """

        :param request:
        :return:
        """
        # 1、接收参数（转化为Python中的基本类型）&校验数据
        json_data = request.body  # 接收参数
        python_data = json.loads(json_data, encoding="utf-8")  # 转化为Python中的基本类型
        # 校验数据
        serializer = serializers.ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors, status=400)
        # 2、向数据库中新增项目
        # 可以通过序列化对象中的validated_data属性获取校验通过之后的数据
        # project = Projects.objects.create(**serializer.validated_data)
        # a.在创建序列化对象时，只给data传参
        # b.那么使用序列化对象调用save方法，只调用create()方法
        # c.用于创建项目
        # d.save方法智能传递关键字参数，会被create中的validated_data接收
        # serializer.save（username="小黑"，age=18）
        project = serializer.save()
        # 3、返回结果（将新增项目的数据返回）(反序列化)
        serializer = serializers.ProjectSerializer(instance=project)
        return JsonResponse(serializer.data, status=201)


class ProjectDetail(View):
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        获取指定项目信息
        :param request: 
        :param pk: 
        :return: 
        """""
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = self.get_object(pk)
        # 3. 进行序列化操作
        serializer = serializers.ProjectSerializer(instance=one_project)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """
        更新指定的项目
        :param request:
        :param pk:
        :return:
        """
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = Projects.objects.get(id=pk)
        # 3、接收参数（转化为Python中的基本类型）&校验数据
        json_data = request.body  # 接收参数
        python_data = json.loads(json_data, encoding="utf-8")  # 转化为Python中的字典类型
        # 校验数据
        serializer = serializers.ProjectSerializer(instance=one_project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors, status=400)
        # 4、向数据库中更新项目
        # a. 在创建序列化器对象时, 给instance和data同时传递参数
        # b. 调用save()时, 会自动化调用update()方法
        serializer.save()

        # 5、返回结果（将新增项目的数据序列化返回）
        return JsonResponse(serializer.data, status=201)

    def patch(self, request, pk):
        project_list = []
        return JsonResponse(data=project_list, safe=False)

    def delete(self, request, pk):
        """
        删除指定的数据
        :param request:
        :param pk:
        :return:
        """
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = Projects.objects.get(id=pk)
        # 3、删除项目
        one_project.delete()
        # 4、返回结果（将新增项目的数据返回）
        return JsonResponse(None, safe=False, status=204)
