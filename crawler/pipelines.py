# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from utils import *
from utils import MysqlCon as mysql


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

# 验证是否一个title是否对应一个time和一个link ## 不校验了
class CheckPipeline(object):
    def process_item(self, item, spider):
        if(item):
            cLen = len(item['city'])
            tLen = len(item['title'])
            tmLen = len(item['time'])
            lLen = len(item['link'])

            # print(item['city'], item['title'], item['time'], item['link'])

            if(cLen == tLen & tLen == tmLen & tmLen == lLen):
                return item
                # pass
            else:
                print('校验不通过，数据长度不一致')
                # pass

        else:
            print('no info catch!')


# 去重
# https://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/item-pipeline.html#topics-item-pipeline
class DuplicatesPipeline(object):
    def __init__(self):
        self.links_seen = []

    def process_item(self, item, spider):
        # print(type(item['link']))
        # print(type(self.links_seen))

        # print('item')
        # print(str(item['link']))
        # print('seen')
        # print(self.links_seen)

        if item['link'] in self.links_seen:
            print('alreay in database')
        else:
            self.links_seen.extend(item['link'])
            return item


# 存入mysql数据库
# https://www.cnblogs.com/conanwang/p/6028110.html
class MysqlPipeline(object):
    def __init__(self, mysql_uri, mysql_user, mysql_password, mysql_database, mysql_table):
        # self.mysql_uri = mysql_uri
        # self.mysql_user = mysql_user
        # self.mysql_password = mysql_password
        # self.mysql_database = mysql_database
        self.client = mysql(mysql_uri, mysql_user, mysql_password, mysql_database, mysql_table)
        # print("链接数据库")
    

    def open_spider(self, spider):
        # self.client.dropAllTable()
        pass

        # self.client.openCon()
        # print('ok')
        # print(self.client)
        # self.cursor = self.client.cursor()
        
        # print('spider')
        # print(spider)

        
        # sql = """CREATE TABLE ANQING (
        #  FIRST_NAME  CHAR(20) NOT NULL,
        #  LAST_NAME  CHAR(20),
        #  AGE INT,  
        #  SEX CHAR(1),
        #  INCOME FLOAT )"""

        # cursor.execute(sql)

    def close_spider(self, spider):
        self.client.closeCon()
    
    @classmethod
    def from_crawler(cls, crawler):
        # print(crawler.settings.get('MYSQL_DATABASE'))
        return cls(
            mysql_uri = crawler.settings.get('MYSQL_URI'),
            mysql_user = crawler.settings.get('MYSQL_USER'),
            mysql_password = crawler.settings.get('MYSQL_PASSWORD'),
            mysql_database = crawler.settings.get('MYSQL_DATABASE'),
            mysql_table = crawler.settings.get('MYSQL_TABLE')
        )

    def process_item(self, item, spider):
        # print('connect db!')
        # print(spider)
        # print(item['title'], item['time'], item['link'])
        # test()
        # print(spider.name)
        
        # print('city: %s' % spider.city)
        # self.client.createTable(spider.name)    #不存在则创建数据库 #多次执行，有优化空间 // django创建了，不需要再创建

        # 2018-10-26 00:00 格式化成 2018-10-26
        # 18-10-26 格式化成 2018-10-26
        # print(len(item['time'].strip()))
        item_time = item['time'].strip()

        if(len(item_time) == 16): # it should be equal to 10.
            # print(item['title'], item['time'], item['link'])
            # print(item['time'][0:10])
            item_time = item_time[0:10]
            # self.client.storeIntoMsql(spider.city, item['title'], item['time'][0:10], item['link']) # 存入数据库
        elif(len(item_time) == 10):
            # print(item['title'], item['time'], item['link'])
            # self.client.storeIntoMsql(spider.city, item['title'], item['time'], item['link']) # 存入数据库
            pass
            # print(item['title'], item['time'], item['link'])
        elif(len(item_time) == 8):
            # print('20' + item['time'])
            item_time = '20' + item_time
            # self.client.storeIntoMsql(spider.city, item['title'], '20' + item['time'], item['link']) # 存入数据库
        else:
            print('time field with incorrect length!')


        self.client.storeIntoMsql(spider.city, item['title'], item_time, item['link']) # 存入数据库


        # print('len: %s' % len(item['time']))

        # self.client.storeIntoMsql(spider.city, item['title'], item['time'], item['link']) # 存入数据库
        
        # res = self.client.storeIntoMsql(item['title'], item['time'], item['link'], spider.name) # 存入数据库
        # print('受影响条数：%s' % res) # 1正确 -1错误
        return item


class MonitorPipeline(object):
    # 关键词监测及提醒功能
    pass