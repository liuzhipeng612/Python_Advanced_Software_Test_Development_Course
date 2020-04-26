from rest_framework import serializers

from .models import Testsuits


class TestsuitModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Testsuits
        exclude = ('create_time', 'update_time')


class TestsuitNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testsuits
        fields = ('id', 'name')
