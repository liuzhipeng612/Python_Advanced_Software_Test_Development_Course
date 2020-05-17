from rest_framework import serializers

from .models import Testcases


class TestcaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcases
        exclude = ('create_time', 'update_time')

    def create(self, validated_data):
        response = super().create(validated_data)
        pass

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
        # instance = get_class_time_formatting(instance)
        return instance


class TestcaseNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcases
        fields = ('id', 'name')
