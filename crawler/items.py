# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 字典数据
class AnqingItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class HefeiItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class MaanshanItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class TonglingItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

# 蚌埠返回的地址比较特殊，是绝对地址不是相对地址
class BengbuItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class WuhuItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class SuzhouItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

# 宣城的网站常年打不开
class XuanchengItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

