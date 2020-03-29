"""api_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from rest_framework import routers

# 1.创建SimpleRouter路由对象
# router = routers.SimpleRouter()
# 使用DefaultRouter会自动创建跟路由页面
router = routers.DefaultRouter()
# 2.注册路由
# 第一个一个参数为prefix路由前缀（支持正则表达式），一般添加为应用名即可
# 第二个参数为视图集类（只有视图集类才能支持router）
# 第三个参数为basename，指定url别名前缀
# router.register(r'Projects', views.ProjectViewSet, basename='bs')
router.register(r'', views.ProjectViewSet)

urlpatterns = [
    # path('', views.ProjectViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'})),
    # path('names/', views.ProjectViewSet.as_view({
    #     'get': 'names'})),
    # path('<int:pk>/', views.ProjectViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'})),
    # 3.使用路由对象.url属性获取路由条目
    # path('', include(router.urls)),
]
# 4.或者将url添加到urlpatterns列表中
urlpatterns += router.urls
