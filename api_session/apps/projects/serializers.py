from rest_framework import serializers

from .models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 给系列化器指定名字
        model = Projects

        # 对某些字段进行序列化
        # fields = ()

        # 排除某些字段进行序列化
        exclude = ('create_time', 'update_time', 'desc')
