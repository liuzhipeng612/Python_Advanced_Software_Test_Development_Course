from rest_framework import serializers

from .models import Reports


class ReportModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Reports
        exclude = ('create_time', 'update_time')


class ReportNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ('id', 'name')
