"""django_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title='Lemon API 接口文档平台',  # 必传
        default_version='v1',  # 必传
        description='这是一个美轮美奂的接口文档',
        terms_of_service='http://www.pysdev.com',
        contact=openapi.Contact(email='admin@pysdev.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),  # 权限类
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects',
         include('projects.urls')),  # 将路径为projects的全部指向interfaces子路由
    path('interfaces/',
         include('interfaces.urls')),  # 将路径为interfaces的全部指向interfaces子路由
    path('docs/', include_docs_urls(title='测试平台接口文档')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
