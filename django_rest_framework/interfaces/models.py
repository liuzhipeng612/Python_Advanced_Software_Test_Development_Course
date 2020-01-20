from django.db import models

# Create your models here.
class Interface(models.Model):
    """
    接口模型类
    一个项目中有多个接口
    一个接口对应一个项目
    项目表和接口表的关系：一对多
    需要在“多”的一侧创建外键
    """
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="接口名称", unique=True, help_text="接口名称", max_length=200)
    leader = models.CharField(verbose_name="项目负责人", help_text="项目负责人", max_length=50)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    desc = models.CharField(verbose_name="简要描述", help_text="简要描述", max_length=200, default="", blank=True, null=True)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")