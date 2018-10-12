"""crawlerview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
# from django.
# import url

from .app import index as crawler_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crawler_index.index),   # 显示页面
    # path('api/', include('rest_framework.urls', namespace='rest_framework')),

    path('add/', crawler_index.add),   # 添加mock数据
    path('drop/', crawler_index.drop),   # 删除所有数据表

    path('api/', crawler_index.api),   # get post city数据 api
]

