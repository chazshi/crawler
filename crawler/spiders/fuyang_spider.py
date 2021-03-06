# -*- coding: utf-8 -*-
import scrapy
from crawler.items import FuyangItem

sp_name = 'fuyang'                          # 爬虫名
city = '阜阳'
sp_allowed_domains = ['jyzx.fy.gov.cn']     # 允许访问的域名
sp_start_urls = ['http://jyzx.fy.gov.cn/FuYang/zfcg/011001/']   # 要爬取的页面
# xpath_title = '/html/head/title/text()'                 # 标题，暂时没用上
xpath_list = '//div[@class="ewb-weixin-wrap ewb-container"]/div[@class="ewb-row ewb-mt10"]/div/div[@id="right"]/div/div[@class="con-box"]/ul[@class="wb-data-item"]/li[@class="wb-data-list"]'    # 爬取li的css
# css_list = '.border1 table tbody tr:nth-child(2) td table:nth-child(2) tbody tr'    # 爬取li的css

xpath_item_title = './div[@class="wb-data-infor"]/a/text()'         # li中的主要信息
xpath_item_time = './span[@class="wb-data-date"]/text()'           # li中的时间信息
xpath_item_link = './div[@class="wb-data-infor"]/a/@href'           # li中的链接信息

class FuyangSpider(scrapy.Spider):
    name = sp_name
    city = city
    allowed_domains = sp_allowed_domains
    start_urls = sp_start_urls
    # print('sp run:')
    def parse(self, response):
        
        # print('response: %s' % response.xpath(xpath_list)) 
        # ### 谷歌浏览器会在table标签下自动添加没写的tbody实现规范化，所以不要定位tbody

        for sel in response.xpath(xpath_list):
            # print('sel: %s'% sel)
            item = FuyangItem()
            # print(sel.xpath(xpath_item_title))


            item['title'] = sel.xpath(xpath_item_title).extract()[0]
            item['time'] = sel.xpath(xpath_item_time).extract()[0]
            
            item['link'] = sp_allowed_domains[0] + sel.xpath(xpath_item_link).extract()[0]

            # print(item['title'], item['time'], item['link'])
            # print("time: %s" % item['time'])
            yield item
