from django.db.models import Q
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
    # def get(self, request):
    #     # # 修改操作
    #     # # 方法一
    #     # # 先获取需要更新的模型类对象
    #     # # 然后修改相关属性
    #     # # 对修改的属性进行保存q
    #     # one_project = Projects.objects.get(id=19)
    #     # one_project.leader = "龙的传人"
    #     # one_project.save()
    #     # Projects.objects.filter(id=16).update(leader="可优院士")
    #     return HttpResponse("修改项目成功")
    # def delete(self, request):
    #     # 删除操作
    #     one_project = Projects.objects.get(id=19)
    #     one_project.delete()
    #     return HttpResponse("删除项目成功")
    def get(self, request):
        # 查询操作

        # #一、获取一张表中的所有记录
        # #1、调用all()方法，返回QuerySet对象
        # #2、QuerySet对象相当于一个高性能的列表（惰性加载）,QuerySet对象中存放的是模型类对象
        # #3、支持列表的数字索引功能（返回的是一个模型类对象）、切片操作（返回的依然是一个QuerySet对象）、不支持负值查询
        # #4、QuerySet对象.first()可以获取第一个元素，QuerySet对象.last()获取最后一个元素
        # qs = Projects.objects.all()
        # for i in qs:
        #     print(i.name)

        # # 二、获取某个指定的记录，使用get()
        # # 1、如果没有查询到记录会报错，如果查询到多个记录也会报错，只有返回一条记录才不会报错
        # # 2、返回的是模型类对象
        # # 3、get方法最好使用主键或者唯一键去查询
        # qs = Projects.objects.get(id=1)

        # 三、获取多条记录，使用filter()
        # qs=Projects.objects.filter(id=1)
        # qs=Projects.objects.filter(leader__contains="某人")   #一条数据的某字段中包含xx内容
        # qs = Projects.objects.filter(name__contains=["项目1", "项目2"])  # 查看分别在集合中对应的项目

        # 四、联表查询
        # 将多个条件在同一个filter中指定，为“与”的关系
        # qs=Projects.objects.filter(name__contains="项目",id__gt=10)
        # 一个QuerySet对象支持链式操作，可以同时调用多个filter
        # qs = Projects.objects.filter(name__contains="项目").filter(id__gt=10)
        # 或的关系需要时用Q变量
        # qs = Projects.objects.filter(Q(name__contains="项目") | Q(id__gt=10))

        # 五、多表关联查询
        # 使用从表的条件来查找父表的数据
        # 使用从表模型类名小写__从表字段名__条件运算符
        # qs=Projects.objects.filter(interfaces__name__contains="注册")

        # 六、获取查询集对象的数量
        # 使用查询集对象调用count()方法获取查询集中的数据条数
        # qs = Projects.objects.filter(name__contains="项目").count()

        # 七、排序操作
        # 可以使用查询集对象调用order_by()方法来对查询集进行排序
        # 默认是升序排列，如果需要降序排列，可以在字段名前加-
        qs = Projects.objects.filter(name__contains="项目").order_by("-id")
        return HttpResponse("查询项目成功")
