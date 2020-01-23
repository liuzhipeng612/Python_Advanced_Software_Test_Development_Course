from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
    return HttpResponse("<h1>可优村长你好啊！这个是函数视图GET方法请求的结果</h1>")


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是类视图GET方法请求的结果</h1>")

    def post(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是类视图POST方法请求的结果</h1>")

    def put(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是类视图PUT方法请求的结果</h1>")

    def delete(self, request):
        return HttpResponse("<h1>可优村长你好啊！这个是类视图DELETE方法请求的结果</h1>")
