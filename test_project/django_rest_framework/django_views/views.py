import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views import View


# Create your views here.

# def index(request):
#     if request.method == "GET":
#         return HttpResponse("<h1这个是GET方法请求的返回结果</h1>")
#     elif request.method == "POST":
#         return HttpResponse("<h1>这个是POST方法请求的返回结果</h1>")
#     elif request.method == "PUT":
#         return HttpResponse("<h1>这个是PUT方法请求返回的结果</h1>")


class HomeIndex(View):
    def get(self, request, pk):
        data = {
            'name': 'daodao',
            'age': '18',
            'gender': '男'
        }
        return JsonResponse(data, safe=False)
        # return HttpResponse("<h1>这个是GET方法请求的返回结果</h1>")

    def post(self, request, pk):
        # print(json.loads(request.body.decode('utf-8')))
        print(pk)
        return HttpResponse(content="<h1>这个是POST方法请求的返回结果</h1>", content_type=tuple)

    def put(self, request):
        return HttpResponse("<h1>这个是PUT方法请求返回的结果</h1>")
