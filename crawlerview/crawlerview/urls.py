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

    # api
    path('infos/add/', crawler_index.add),   # 添加mock数据
    path('infos/drop/', crawler_index.drop),   # 删除所有数据表

    path('infos/', crawler_index.infos),   # get post city数据 api
    path('infos/citys', crawler_index.citys)
    # path('infos/')


    # TODO: 增加【增加地区】页面，增加【获取今天最新】功能，增加【提醒设置】功能
]

