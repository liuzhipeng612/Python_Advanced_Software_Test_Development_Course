import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View

from interfaces.models import Interfaces
from projects.models import Projects
from . import serializers


class ProjectList(View):
    def get(self, request):
        # 1、从数据库中获取所有项目的信息
        project_qs = Projects.objects.all()
        # 2、将模型类对象转化为字典类型，构造嵌套字典的列表
        # project_list = []
        # for project in project_qs:
        #     # one_list = {
        #     #     "id": project.id,
        #     #     "name": project.name,
        #     #     "leader": project.leader,
        #     #     "tester": project.tester,
        #     #     "programmer": project.programmer,
        #     #     "publish_app": project.publish_app,
        #     #     "desc": project.desc
        #     # }
        #     # project_list.append(one_list)
        #     project_list.append({
        #         "id": project.id,
        #         "name": project.name,
        #         "leader": project.leader,
        #         "tester": project.tester,
        #         "programmer": project.programmer,
        #         "publish_app": project.publish_app,
        #         "desc": project.desc
        #     })
        # 如果返回多条数据(列表数据), 那么需要添加many为True
        serializer = serializers.ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    def post(self, request):
        # q1、前端要不要传参？肯定要
        # q2、前端要以那种形式来传参？在请求体中以json形式来传参
        # 1、接收参数（转化为Python中的基本类型）&校验数据
        json_data = request.body  # 接收参数
        python_data = json.loads(json_data, encoding="utf-8")  # 转化为Python中的基本类型
        # 校验数据
        serializer = serializers.ProjectSerializer(data=python_data)
        serializer.is_valid()
        # 2、向数据库中新增项目
        # 方法一
        # project_name = python_data["name"]
        # project_leader = python_data["leader"]
        # project_tester = python_data["tester"]
        # project_programmer = python_data["programmer"]
        # project_publish_app = python_data["publish_app"]
        # project_desc = python_data["desc"]
        #
        # one_project = Projects(name=project_name,
        #                        leader=project_leader,
        #                        tester=project_tester,
        #                        programmer=project_programmer,
        #                        publish_app=project_publish_app,
        #                        desc=project_desc)
        # one_project.save()
        # 方法二
        project = Projects.objects.create(**python_data)
        # 3、返回结果（将新增项目的数据返回）(反序列化)
        # one_dict = {
        #     "id": project.id,
        #     "name": project.name,
        #     "leader": project.leader,
        #     "tester": project.tester,
        #     "programmer": project.programmer,
        #     "publish_app": project.publish_app,
        #     "desc": project.desc
        # }
        serializer = serializers.ProjectSerializer(instance=project)
        return JsonResponse(serializer.data, status=201)


class ProjectDetail(View):
    # 方案一
    # 如果pk值存在，返回对应pk值得项目
    # 如果pk值不存在，返回{"msg": "项目ID不存在"}的json格式数据
    # 调用get_object()方法是，需要判断one_project是否为JsonResponse对象，即异常的JsonResponse对象，如果是直接返回one_project,
    # def get_object(self, pk):
    #     try:
    #         one_project = Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         return JsonResponse({"msg": "项目ID不存在"}, status=400)
    #     return one_project
    # 方案二
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # 获取指定项目信息
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = self.get_object(pk)
        # 方案一
        # if isinstance(one_project, JsonResponse):
        #     return one_project
        # 3、将模型类对象转换成字典（反序列化）
        # one_dict = {
        #     "id": one_project.id,
        #     "name": one_project.name,
        #     "leader": one_project.leader,
        #     "tester": one_project.tester,
        #     "programmer": one_project.programmer,
        #     "publish_app": one_project.publish_app,
        #     "desc": one_project.desc
        # }
        # 3. 进行序列化操作
        # a. 序列化过程: 将模型类对象(或者查询集对象)转化为json格式数据
        # b. 将模型类对象(或者查询集对象)传给instance, 可以进行序列化操作
        # c. 通过序列化器ProjectSerializer对象的data属性, 可以获取转化之后的数据
        serializer = serializers.ProjectSerializer(instance=one_project)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        # 更新指定的项目
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = Projects.objects.get(id=pk)
        # q1、前端要不要传参？肯定要
        # q2、前端要以那种形式来传参？在请求体中以json形式来传参
        # 3、接收参数（转化为Python中的基本类型）&校验数据
        json_data = request.body  # 接收参数
        python_data = json.loads(json_data, encoding="utf-8")  # 转化为Python中的字典类型
        # 4、向数据库中更新项目
        one_project.name = python_data["name"]
        one_project.leader = python_data["leader"]
        one_project.tester = python_data["tester"]
        one_project.programmer = python_data["programmer"]
        one_project.publish_app = python_data["publish_app"]
        one_project.desc = python_data["desc"]
        one_project.save()
        # 5、返回结果（将新增项目的数据返回）(反序列化)
        # one_dict = {
        #     "id": one_project.id,
        #     "name": one_project.name,
        #     "leader": one_project.leader,
        #     "tester": one_project.tester,
        #     "programmer": one_project.programmer,
        #     "publish_app": one_project.publish_app,
        #     "desc": one_project.desc
        # }
        serializer = serializers.ProjectSerializer(instance=one_project)
        return JsonResponse(serializer.data, status=201)

    def patch(self, request, pk):
        project_list = []
        return JsonResponse(data=project_list, safe=False)

    def delete(self, request, pk):
        # 删除指定的数据
        # 1、校验前端传递的pk（项目ID）值
        # 2、获取指定pk值得项目
        one_project = Projects.objects.get(id=pk)
        # 3、删除项目
        one_project.delete()
        # 4、返回结果（将新增项目的数据返回）
        return JsonResponse(None, safe=False, status=204)
