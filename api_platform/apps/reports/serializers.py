from rest_framework import serializers

from .models import Reports


class ReportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        exclude = ('update_time', 'html')
