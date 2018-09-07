# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from utils import *
import utils


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

# 验证是否一个title是否对应一个time和一个link
class CheckPipeline(object):
    def process_item(self, item, spider):
        if(item):
            tLen = len(item['title'])
            tmLen = len(item['time'])
            lLen = len(item['link'])

            # print(item['title'], item['time'], item['link'])

            if(tLen == tmLen & tmLen == lLen):
                return item
                # pass
            else:
                print('校验不通过，数据长度不一致')
                # pass

        else:
            print('no information')


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
# http://www.runoob.com/python/python-mysql.html
class MysqlPipeline(object):
    def __init__(self, mysql_uri, mysql_user, mysql_password, mysql_database):
        # self.mysql_uri = mysql_uri
        # self.mysql_user = mysql_user
        # self.mysql_password = mysql_password
        # self.mysql_database = mysql_database
        self.client = utils.MysqlCon(mysql_uri, mysql_user, mysql_password, mysql_database)


    def open_spider(self, spider):
        self.client.openCon()
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
            mysql_database = crawler.settings.get('MYSQL_DATABASE')
        )

    def process_item(self, item, spider):
        # print(spider)
        # print(item['title'], item['time'], item['link'])
        # test()
        # print(spider.name)
        
        self.client.createTable(spider.name)


        return item