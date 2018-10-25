# -*- coding: utf-8 -*-
import scrapy
from crawler.items import AnqingItem

sp_name = 'anqing'                          # 爬虫名
city = '安庆'
sp_allowed_domains = ['www.aqzbcg.org:1102']     # 允许访问的域名
sp_start_urls = ['http://www.aqzbcg.org:1102/jyxx/012002/012002001/project.html']   # 要爬取的页面
# xpath_title = '/html/head/title/text()'                 # 标题，暂时没用上
xpath_list = '//div[@class="ewb-span18 ewb-ml10"]//ul[@class="wb-data-item"]//li[@class="wb-data-list"]'    # 爬取li的css
# css_list = '.ewb-span18 .wb-data-item .wb-data-list'    # 爬取li的css
xpath_item_title = './div/a/text()'         # li中的主要信息
xpath_item_time = './span/text()'           # li中的时间信息
xpath_item_link = './div/a/@href'           # li中的链接信息

class AnqingSpider(scrapy.Spider):
    name = sp_name
    city = city
    allowed_domains = sp_allowed_domains
    start_urls = sp_start_urls

    def parse(self, response):
        # 提取数据

        ## 提取标题数据
        # title = response.xpath(xpath_title).extract()[0]
        # print(title)
        ## 保存文件
        # filename = str(title) + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        
        # print(len(response.css('.ewb-span18 .wb-data-item .wb-data-list')))
        
        # 提取重要数据
        for sel in response.xpath(xpath_list):
            # print(sel)
            item = AnqingItem()
            item['title'] = sel.xpath(xpath_item_title).extract()[0]
            item['time'] = sel.xpath(xpath_item_time).extract()[0]
            
            item['link'] = sp_allowed_domains[0] + sel.xpath(xpath_item_link).extract()[0]

            yield item
