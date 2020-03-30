from rest_framework import serializers

from .models import Interfaces
from projects.models import Projects


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class InterfacesModelSerializer(serializers.ModelSerializer):
    # a.会自动将外检字段生成PrimaryKeyRelatedField类型，返回的是外键对应的id值
    # project=serializersPrimaryKeyRelatedField（help_text="所属项目",queryset=Projects.objects.all()）
    # b.会自动调用外键的__str__方法
    # project = serializers.StringRelatedField(label="所属项目")
    # c.如果子表需要获得外键ID对应父表的 使用父表的模型序列化器来创建
    project = ProjectsModelSerializer(read_only=True)

    class Meta:
        # 1. 指定参照哪一个模型
        model = Interfaces
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'error_messages': {'max_length': '接口名称的长度不能操作200个字节!'},
                'max_length': 50,
            },
            'leader': {
                'label': '负责人',
                'write_only': True
            }
        }

        # def create(self, validated_data):
        #     """
        #     创建项目
        #     :param validated_data: 校验通过之后的项目数据
        #     :return: 项目创建成功之后的模型类对象
        #     """
        #     interface = Interfaces.objects.create(**validated_data)
        #     return interface

        # def update(self, instance, validated_data):
        #     """
        #     更新项目
        #     :param instance: 待更新的项目模型类对象
        #     :param validated_data: 校验通过之后的项目数据
        #     :return: 项目更新成功之后的模型类对象
        #     """
        #     instance.name = validated_data["name"]
        #     instance.tester = validated_data["tester"]
        #     instance.desc = validated_data["desc"]
        #     instance.project = validated_data["project"]
        #     instance.save()
        #     return instance
