# -*- coding: utf-8 -*-
import scrapy
from crawler.items import SuzhouItem

sp_name = 'suzhou'                          # 爬虫名
city = '宿州'
sp_allowed_domains = ['www.szggzyjy.cn']     # 允许访问的域名
sp_start_urls = ['http://www.szggzyjy.cn/szfront/jyxx/002001/002001002/002001002001/']   # 要爬取的页面
# xpath_title = '/html/head/title/text()'                 # 标题，暂时没用上
xpath_list = '//div[@class="ewb-row ewb-mt6"]/div[@class="ewb-span18 r"]/div[@class="ewb-list-bd"]/div/ul[@class="ewb-lbd-items"]/li[@class="clearfix"]'    # 爬取li的css    # 爬取li的css
# css_list = '.border1 table tbody tr:nth-child(2) td table:nth-child(2) tbody tr'    # 爬取li的css

xpath_item_title = './a/text()'         # li中的主要信息
xpath_item_time = './span[@class="ewb-ndate r"]/text()'           # li中的时间信息
xpath_item_link = './a/@href'           # li中的链接信息

class WuhuSpider(scrapy.Spider):
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
            item = SuzhouItem()
            # print(sel.xpath(xpath_item_title))


            item['title'] = sel.xpath(xpath_item_title).extract()[0]
            item['time'] = sel.xpath(xpath_item_time).extract()[0]
            
            item['link'] = sp_allowed_domains[0] + sel.xpath(xpath_item_link).extract()[0]

            # print(item['title'], item['time'], item['link'])
            # print("time: %s" % item['time'])
            yield item
