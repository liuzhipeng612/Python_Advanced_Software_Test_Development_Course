from django.http import HttpResponse, JsonResponse
from django.views import View

from interfaces.models import Interfaces
from projects.models import Projects


class IndexView(View):
    # # 创建操作
    #
    # # 方法一
    # # 一个模型类相当于一个表（table）
    # # 一个模型类对象相当于一条数据（record）
    # def get(self, request):
    #     one_project = Projects(name="国产大飞机", leader="xxx院士", tester="所见", programmer="龙的传人",
    #                            publish_app="国产大飞机C919应用", desc="项目简介")
    #     # 调用模型类对象save()才能执行sql语句
    #     one_project.save()
    #     # 方法二
    #     one_project = Projects.objects.create(name="国产大飞机3", leader="xxx院士", tester="所见", programmer="龙的传人",
    #                                           publish_app="国产大飞机C919应用", desc="项目简介")
    #     Interfaces.objects.create(name="国产大飞机C919登录接口", tester="Addoil", project=one_project)
    #     # Interfaces.objects.create(name="国产大飞机C919登录接口", tester="Addoil", project_id=17)
    #     return HttpResponse("创建项目成功")
    def get(self, request):
        # # 修改操作
        # # 方法一
        # # 先获取需要更新的模型类对象
        # # 然后修改相关属性
        # # 对修改的属性进行保存
        # one_project = Projects.objects.get(id=19)
        # one_project.leader = "龙的传人"
        # one_project.save()
        Projects.objects.filter(id=16).update(leader="可优院士")
        return HttpResponse("修改项目成功")
