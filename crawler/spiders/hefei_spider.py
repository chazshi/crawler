# -*- coding: utf-8 -*-
import scrapy
from crawler.items import HefeiItem

sp_name = 'hefei'                           # 爬虫名
sp_allowed_domains = ['ggzy.hefei.gov.cn']  # 允许访问的域名
sp_start_urls = ['http://ggzy.hefei.gov.cn/jyxx/002002/002002001/moreinfo_jyxxgg.html']      # 要爬取的页面
xpath_title = '/html/head/title/text()'         # 标题，暂时没用上
css_list = '.ewb-right-item .ewb-right-list'    # 爬取li的css
xpath_item_title = './a/span[last()]/text()'         # li中的主要信息
xpath_item_time = './span/text()'           # li中的时间信息
xpath_item_link = './a/@href'           # li中的链接信息

class HefeiSpider(scrapy.Spider):
    name = sp_name
    allowed_domains = sp_allowed_domains
    start_urls = sp_start_urls


    # 代理
    # def __init__(self):
    #     self.headers = {
    #         "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         "Accept-Encoding": 'gzip, deflate',
    #         "Accept-Language": 'zh-CN,zh;q=0.9',
    #         "Cache-Control": 'max-age=0',
    #         "Connection": 'keep-alive',
    #         "Cookie": 'fontZoomState=0',
    #         "Host": 'ggzy.hefei.gov.cn',
    #         "If-Modified-Since": 'Fri, 07 Sep 2018 05:43:51 GMT',
    #         # "If-None-Match": 'W/"5b921017-67b9"',
    #         "Upgrade-Insecure-Requests": '1',
    #         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',


    #         # "Remote Address": '60.166.8.61:80',
    #         # "Host": sp_allowed_domains[0],
    #         # "Referer": 'http://'  + sp_allowed_domains[0],
    #         # 'Content-Type':'text/html; charset=utf-8',
    #         # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    #     }
 


    def parse(self, response):
        # 提取数据

        ## 提取标题数据
        title = response.xpath(xpath_title).extract()[0]

        # print(title)
        ## 保存文件
        filename = str(title) + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        
        # print(len(response.css('.ewb-span18 .wb-data-item .wb-data-list')))
        
        # 提取重要数据
        for sel in response.css(css_list):
            # print(sel)
            item = HefeiItem()
            item['title'] = sel.xpath(xpath_item_title).extract()[0]
            item['time'] = sel.xpath(xpath_item_time).extract()[0]

            # print(type(sp_allowed_domains[0]))
            # print(type(sel.xpath(xpath_item_link).extract()[0]))


            item['link'] = sp_allowed_domains[0] + sel.xpath(xpath_item_link).extract()[0]
            # print(item['title'], item['time'], item['link'])
            yield item
