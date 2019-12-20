from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

# 函数视图
# def index(request):
#     return HttpResponse("<h1>可优村长你好啊！</h1>")

# 类视图
class HomeIndex(View):
    def get(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是GET方法请求的结果</h1>")

    def post(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是POST方法请求的结果</h1>")
