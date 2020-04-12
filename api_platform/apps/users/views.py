from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class RegisterView(CreateAPIView):
    """
    注册接口
    """
    serializer_class = serializers.RegisteSerializer
    # 如果某个视图中, 没有获取信息的接口, 那么可以不用指定queryset类属性


class UsernameValidateView(APIView):
    def get(self, request, username):
        data = {
            "username": username,
            "count": User.objects.filter(username=username).count()
        }
        return Response(data)


class EmailValidateView(APIView):
    def get(self, request, email):
        data = {
            "username": email,
            "count": User.objects.filter(username=email).count()
        }
        return Response(data)
