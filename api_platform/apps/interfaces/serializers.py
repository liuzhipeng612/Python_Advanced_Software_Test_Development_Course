from rest_framework import serializers

from projects.models import Projects
from .models import Interfaces
from .utils import get_class_time_formatting


class InterfaceModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(label='所属项目名称', help_text='所属项目名称')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), label='项目id', help_text='项目id',
                                                    write_only=True)

    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester', 'desc', 'project', 'project_id', 'create_time')

    def create(self, validated_data):
        validated_data['project_id'] = validated_data['project_id'].id
        interface = Interfaces.objects.create(**validated_data)
        interface = get_class_time_formatting(interface)
        return interface

    def update(self, instance, validated_data):
        """
        更新项目
        :param instance: 待更新的项目模型类对象
        :param validated_data: 校验通过之后的项目数据
        :return: 项目更新成功之后的模型类对象
        """
        instance.name = validated_data["name"]
        instance.tester = validated_data["tester"]
        instance.desc = validated_data["desc"]
        instance.project = validated_data["project_id"]
        instance.save()
        instance = get_class_time_formatting(instance)
        return instance
