from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from projects.models import Projects


def index(request):
    return HttpResponse("<h1>可优村长你好啊！这个是函数视图GET方法请求的结果</h1>")


# 演练ORM中的CRUD相关操作
class IndexView(View):
    def get(self, request):
        # 修改操作
        # 方法一
        revise = Projects.objects.get(name="Django框架")
        revise.leader = "keyou村长"
        revise.save()
        # 方法二
        Projects.objects.filter(name__contains="rest").update(leader="keyou村长")
        return HttpResponse("<h1>可优村长你好啊！这个是类视图GET方法请求数据库表修改数据的结果</h1>")

    def post(self, request):
        # 查询操作
        # 方法一
        inquiry = Projects.objects.all()
        print(inquiry)
        # 方法二
        try:
            inquiry = Projects.objects.get(name__endswith="框架")
            print(inquiry)
        except:
            print("不存在以'框架'结尾的数据")
        # 方法三
        inquiry = Projects.objects.filter(name__regex=r'^(Django|项目)')
        print(inquiry)
        return HttpResponse("<h1>可优村长你好啊！这个是类视图POST方法请求的结果</h1>")

    def put(self, request):
        # 新增操作
        # 方法一
        add = Projects(name="Django框架", leader="可优村长", tester="刀刀村民", programmer="敏敏村民", publish_app="测开APP",
                       desc="框架介绍")
        add.save()

        # 方法二
        Projects.objects.create(name="Django-rest-framework", leader="可优村长", tester="刀刀村民", programmer="敏敏村民",
                                publish_app="测开APP", desc="rest-framework-desc")
        return HttpResponse("<h1>可优村长你好啊！这个是类视图PUT方法请求数据库表新增数据的结果</h1>")

    def delete(self, request):
        # 删除操作
        deletes = Projects.objects.filter(name__in=["Django框架", "Django-rest-framework"])
        deletes.delete()
        return HttpResponse("<h1>可优村长你好啊！这个是类视图DELETE方法请求数据库表数据删除的结果</h1>")
