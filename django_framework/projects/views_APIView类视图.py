import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from interfaces.models import Interfaces
from projects.models import Projects
from . import serializers


class ProjectList(APIView):
    def get(self, request):
        """

        :param request:
        :return:
        """
        # 1、从数据库中获取所有项目的信息
        project_qs = Projects.objects.all()
        # 2、将模型类对象转化为字典类型，构造嵌套字典的列表-反序列化
        serializer = serializers.ProjectModelSerializer(instance=project_qs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        """

        :param request:
        :return:
        """
        # 1、接收参数（转化为Python中的基本类型）&校验数据
        # json_data = request.body  # 接收参数
        # python_data = json.loads(json_data, encoding="utf-8")  # 转化为Python中的基本类型
        # 校验数据
        # serializer = serializers.ProjectModelSerializer(data=python_data)
        # 1.继承DRF框架中的APIView之后，request是DRF中的request对象
        # 2.Response对HttpRequest进行了拓展，HttpRequest有的功能Response都支持
        # 3.不管前端传json还是x-www-form菜蔬，统一使用request.data
        serializer = serializers.ProjectModelSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 2、向数据库中新增项目
        # 可以通过序列化对象中的validated_data属性获取校验通过之后的数据
        # project = Projects.objects.create(**serializer.validated_data)
        # a.在创建序列化对象时，只给data传参
        # b.那么使用序列化对象调用save方法，只调用create()方法
        # c.用于创建项目
        # d.save方法智能传递关键字参数，会被create中的validated_data接收
        # serializer.save（username="小黑"，age=18）
        serializer.save()
        # 3、返回结果（将新增项目的数据返回）(反序列化)
        return Response(serializer.data, status=201)


class ProjectDetail(APIView):
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
        serializer = serializers.ProjectModelSerializer(instance=one_project)
        # 默认请求投中没有Accept，那么返回json
        # 如果请求头中添加了Accept，那么会以Accept指定的格式返回
        return Response(serializer.data)

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
        serializer = serializers.ProjectModelSerializer(instance=one_project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors, status=400)
        # 4、向数据库中更新项目
        # a. 在创建序列化器对象时, 给instance和data同时传递参数
        # b. 调用save()时, 会自动化调用update()方法
        serializer.save()

        # 5、返回结果（将新增项目的数据序列化返回）
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        project_list = []
        return Response(data=project_list)

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
        return Response(None, status=status.HTTP_204_NO_CONTENT)
