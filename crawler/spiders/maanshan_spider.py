# -*- coding: utf-8 -*-
import scrapy
from crawler.items import MaanshanItem

sp_name = 'maanshan'                          # 爬虫名
city = '马鞍山'
sp_allowed_domains = ['zbcg.mas.gov.cn']     # 允许访问的域名
sp_start_urls = ['http://zbcg.mas.gov.cn/maszbw/jygg/028002/028002001/']   # 要爬取的页面
# xpath_title = '/html/head/title/text()'                 # 标题，暂时没用上
xpath_list = '//td[@class="border1"]/table//tr/td/table//tr/td/table//tr/td[@valign="top"]/table//tr'    # 爬取li的css
# css_list = '.border1 table tbody tr:nth-child(2) td table:nth-child(2) tbody tr'    # 爬取li的css
xpath_item_title = './td[@class="TDStyle"]/a/text()'         # li中的主要信息
xpath_item_time = './td[@align="right"]/font/text()'           # li中的时间信息
xpath_item_link = './td[@class="TDStyle"]/a/@href'           # li中的链接信息

class MaanshanSpider(scrapy.Spider):
    name = sp_name
    city = city
    allowed_domains = sp_allowed_domains
    start_urls = sp_start_urls
    # print('sp run:')
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
        # print('response: %s'% response)
        # 提取重要数据

        # print('response: %s' % response.xpath(xpath_list)) 
        # ### 谷歌浏览器会在table标签下自动添加没写的tbody实现规范化，所以不要定位tbody

        for sel in response.xpath(xpath_list):
            # print('sel: %s'% sel)
            item = MaanshanItem()
            item['title'] = sel.xpath(xpath_item_title).extract()[0]
            item['time'] = sel.xpath(xpath_item_time).extract()[0]
            
            item['link'] = sp_allowed_domains[0] + sel.xpath(xpath_item_link).extract()[0]

            # print(item['title'], item['time'], item['link'])
            # print("time: %s" % item['time'])
            yield item
