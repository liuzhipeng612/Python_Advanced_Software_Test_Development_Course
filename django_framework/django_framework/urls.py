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
from django.urls import path, include
from homeworks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('homeworks/',index),
    # path('homeworks/',IndexView.as_view())
    path('homeworks/', include('homeworks.urls')),
    path('projects/', include('projects.urls')),
    path('interfaces/', include('interfaces.urls')),
]