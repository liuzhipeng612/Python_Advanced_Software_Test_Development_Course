from rest_framework import serializers

from .models import Testcases


class TestcaseModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Testcases
        exclude = ('create_time', 'update_time')


class TestcaseNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcases
        fields = ('id', 'name')
