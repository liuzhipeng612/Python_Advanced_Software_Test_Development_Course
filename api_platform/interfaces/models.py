from django.db import models
# from projects.models import Projects


class Interfaces(models.Model):
    id = models.AutoField(verbose_name="id主键",
                          primary_key=True,
                          help_text="id主键")
    name = models.CharField(verbose_name="接口名称",
                            unique=True,
                            help_text="接口名称",
                            max_length=200)
    tester = models.CharField(verbose_name="测试人员",
                              help_text="测试人员",
                              max_length=50)
    desc = models.CharField(verbose_name="简要描述",
                            help_text="简要描述",
                            max_length=200,
                            default="",
                            blank=True,
                            null=True)
    project = models.ForeignKey('projects.Projects',
                                on_delete=models.CASCADE,
                                related_name="interfaces",
                                help_text="所属项目")
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name="创建时间",
                                       help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name="更新时间",
                                       help_text="更新时间")

    class Meta:
        db_table = "tb_interfaces"
        verbose_name = "接口"

    def __str__(self):
        return self.name
