from django.db import models
from projects.models import Projects


# Create your models here.
class Interfaces(models.Model):
    """
    接口模型类
    一个项目中有多个接口
    一个接口对应一个项目
    项目表和接口表的关系：一对多
    需要在“多”的一侧创建外键
    """
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="接口名称", unique=True, help_text="接口名称", max_length=200)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    desc = models.CharField(verbose_name="简要描述", help_text="简要描述", max_length=200, default="", blank=True, null=True)
    # ForeiKey第一个参数为“应用名.模型类”--不需要导入模型类，或者“模型类”--需要导入模型类
    # on_delete设置当附表（项目表）中的数据被删除后，从表该字段的处理方式
    # models.CASCADE子表也会自动删除
    # models.SET_NULL子表会自动设置为NULL
    # related_name指定父表对子表引用名，如果不指定，默认为子表模型类名小写_set（interfaces_set）
    # project = models.ForeignKey(Projects)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name="interfaces",
                                help_text="所属项目")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    class Meta:
        db_table = "tb_interfaces"
        verbose_name = "接口"

    # 连表查询使用python console导入两个表
    # from projects.models import Projects 被导入的Projects表
    # from interfaces.models import Interfaces 被导入的Interfaces表
    # Projects.objects.all()    查看Projects的所有对象信息
    # Projects.objects.get(id=1)    查看Projects表中id=1的对象
    def __str__(self):  # 直接打印名称
        return self.name
    # CRUD对应数据库的语句
    # C->create->insert into
    # R->read->select
    # U->update->update
    # D->delete->delete
