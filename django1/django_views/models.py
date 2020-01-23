from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Projects(models.Model):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="项目名称", unique=True, help_text="项目名称", max_length=200)
    leader = models.CharField(verbose_name="项目负责人", help_text="项目负责人", max_length=50)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    programmer = models.CharField(verbose_name="开发人员", help_text="开发人员", max_length=50)
    publish_app = models.CharField(verbose_name="发布应用", help_text="发布应用", max_length=100)
    desc = models.CharField(verbose_name="简要描述", help_text="简要描述", max_length=200, default="", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")


class TestTeam(models.Model):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="团队名称", unique=True, help_text="团队名称", max_length=200)
    leader = models.CharField(verbose_name="负责人", help_text="负责人", max_length=50)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    module_name = models.CharField(verbose_name="模块名称", help_text="模块名称", max_length=200)
    group_leader = models.CharField(verbose_name="小组长", help_text="小组长", max_length=50, unique=True)
    desc = models.CharField(verbose_name="简要描述", help_text="简要描述", max_length=200, default="", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    review_time = models.DateTimeField(auto_now=True, verbose_name="审核时间", help_text="审核时间")

    class Meta:
        # 可以在Meta中使用db_table自定义表名
        # the database needs something to populate existing rows
        # 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        # 2) Quit, and let me add a default in models.py
        # Invalid input: name 't' is not defined
        # Please enter the default value now, as valid Python
        # The datetime and django1.utils.timezone modules are available, so you can do e.g. timezone.now

        db_table = "django_views_TestTeams"
        verbose_name = "测试团队"
