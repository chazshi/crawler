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

# mysql配置项
MYSQL_URI = msetting.MYSQL_URI
MYSQL_USER = msetting.MYSQL_USER
MYSQL_PASSWORD = msetting.MYSQL_PASSWORD
MYSQL_DATABASE = msetting.MYSQL_DATABASE

from utils import MysqlCon as mysql

client = mysql(MYSQL_URI, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
result = client.getAllItems('anqing')
print(type(result))


client.closeCon()   # 执行完毕清除数据

def index(request):
    context = {}
    context['items'] = result
    return render(request, 'dashboard.html', context)