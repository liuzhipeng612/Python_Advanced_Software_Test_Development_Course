from django.http import HttpResponse
from django.views import View


# 类视图,同时需要导入View
class Index(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World</h1>")
