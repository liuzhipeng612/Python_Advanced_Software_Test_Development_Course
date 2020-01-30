from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Projects


def is_unique_project_name(value):
    """
    创建自定义校验器
    :param value: 待校验的项目名称
    :return:
    """
    qs = Projects.objects.filter(name=value)
    if qs:  # 如果查询集不为空, 那么说明当前项目名已经存在
        raise serializers.ValidationError("项目名不能重复!")


def cotain_keyword_project_name(value):
    """
    创建自定义校验器
    校验项目与名称中是否包含"项目"
    :param value:
    :return:
    """
    if "项目" not in value:
        raise serializers.ValidationError("项目名称中不包含'项目'!")


class ProjectSerializer(serializers.Serializer):
    """创建项目序列化器
    序列化器的作用:
    a. 序列化操作
    b. 反序列化操作
    """
    # 1. 定义的序列化器类, 需要继承Serializer或者Serializer子类
    # 2. 定义的每一个类属性要与模型类中对应
    # 3. label、help_text选项相当于verbose_name, help_text
    # 4. 默认情况下, 定义了哪些类属性(序列化器字段), 那么就会序列化输出哪些字段和哪些字段需要进行反序列化输入
    # a. 如果不需要序列化输出, 不定义即可
    # b. 如果在定义的字段中, 添加write_only选项为True, 那么当前字段只能进行反序列化(数据校验), 不进行序列化输出
    # c. 如果在定义的字段中, 添加read_only选项为True, 那么当前字段只能进行序列化输出, 而不进行反序列化输入(数据校验)
    # id = serializers.IntegerField(label='ID', read_only=True)
    # d. 通过制定validators选项, 使用内置的校验器(UniqueValidator)来校验, 为一个列表
    # e. validators列表中的校验器校验顺序是按照列表的元素顺序, 并且会遍历调用每一个校验器(不管校验成功还是失败, 都会去做校验)
    # name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称',
    # validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名不能重复"), is_unique_project_name])

    name = serializers.CharField(label='项目名称', max_length=20, help_text='项目名称',
                                 validators=[is_unique_project_name, cotain_keyword_project_name])

    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programmer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', allow_null=True, allow_blank=True, default='', help_text='简要描述')

    def validate_name(self):
        pass
