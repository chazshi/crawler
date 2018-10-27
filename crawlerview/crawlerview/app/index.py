from django.http import HttpResponse
from django.shortcuts import render

import sys,os
pwd = os.getcwd() # 获取当前路径
# father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# print("pwd： %s" % pwd)
# print("father_path： %s" % father_path)
sys.path.append(pwd)
# print("sys.path： %s" % sys.path)

from settings import Settings as msetting
# print(msetting.MYSQL_DATABASE)

import json,pickle #导入模块。

# mysql配置项
MYSQL_URI = msetting.MYSQL_URI
MYSQL_USER = msetting.MYSQL_USER
MYSQL_PASSWORD = msetting.MYSQL_PASSWORD
MYSQL_DATABASE = msetting.MYSQL_DATABASE


# client = mysql(MYSQL_URI, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
# result = client.getAllItemsByTableName('city_anqing')
# # print(type(result)) # tuple


# client.closeCon()   # 执行完毕清除数据

from Infos.models import Infos

import datetime
import random
import copy


from .serializers import InfosSerializer

from .serializers import CitysSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from rest_framework import serializers

result = '123'

# python manage.py runserver
def drop(request):
    drop = Infos.objects.filter(title__contains="测试数据")

    context = {}
    context['items'] = copy.copy(drop)   # 浅拷贝，直接等号会被引用，删掉原始对象就不能打印了
    # for item in context['items']:
        # print(item.title)

    drop.delete()

    return render(request, 'dropdata.html', context)

def add(request):
    infos = Infos( city="安庆", title="测试数据%s" % random.randrange(1,100,1), time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), link="www.baidu.com/%s" % random.randrange(1,100,1))
    infos.save()

    print("infos")
    print(infos.title)

    context = {}
    context['items'] = [infos, ]   #create(request)
    return render(request, 'addmock.html', context)

def index(request):

    infos = Infos.objects.all()

    context = {}
    context['items'] = infos   #create(request)
    return render(request, 'dashboard.html', context)


def citys(request, format=None):

    if request.method == 'GET':

        snippets = Infos.objects.values("city").distinct()
        # print('snippets: %s'%snippets)
        # # return snippets

        # L = []
        # for l in snippets:
        #     L.append(l)
        # print(L)
        
        serializer = CitysSerializer(snippets, many=True)
        # print('serializer.data: %s'%serializer.data)    
        # serializer = CitysSerializer(L, many=False)
        
        return JsonResponse(serializer.data, safe=False)
    #     return JSONRenderer().render(serializer.data)

    # elif request.method == 'POST':
    #     pass

def infos(request, format=None):
    print(request)
    # print(date)
    if request.method == 'GET':
        # print(request.GET.get('date'))
        
        if(request.GET.get('date')):
            # 大于今天
            snippets = Infos.objects.filter(time__gte=request.GET.get('date'))
        else:
            snippets = Infos.objects.all()

        # snippets = Infos.objects.all()
        # for item in snippets:
        #     print(item.title)
        
        serializer = InfosSerializer(snippets, many=True)
        # print(json.dumps(serializer))

        # for v in serializer.data:
        #     print("v: %s" % v)
        

        return JsonResponse(serializer.data, safe=False)
        # return JSONRenderer().render(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InfosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)