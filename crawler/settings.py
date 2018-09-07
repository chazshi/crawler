# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'


# mysql配置项
MYSQL_URI = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'crawler'


# 代理配置项
IPPOOL=[
	

    # {"ipaddr":"180.118.86.82:9000"},
    # {"ipaddr":"180.76.149.19:8888"},
    # {"ipaddr":"60.184.163.41:9000"},
    # {"ipaddr":"183.154.215.78:9000"},
    # {"ipaddr":"180.118.134.103:9000"},
    # {"ipaddr":"183.129.244.13:10010"},
    # {"ipaddr":"114.235.22.251:9000"},
    # {"ipaddr":"115.223.210.203:9000"},
    # {"ipaddr":"223.150.39.128:9000"},
    # {"ipaddr":"180.118.128.138:9000"},
    # {"ipaddr":"183.129.244.17:41258"},
    # {"ipaddr":"203.195.209.94:8118"},
    # {"ipaddr":"182.139.111.77:9000"},
    # {"ipaddr":"211.161.250.241:8080"},
    # {"ipaddr":"47.95.156.32:3200"},


    
]

# 无效的ip：218.82.33.225   61.152.81.193:9100      61.152.81.193:9100      

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'crawler.pipelines.CrawlerPipeline': 300,
   'crawler.pipelines.CheckPipeline': 400,
   'crawler.pipelines.DuplicatesPipeline': 500,
   'crawler.pipelines.MysqlPipeline': 600,
   
   
}

# DOWNLOADER_MIDDLEWARES = {
# #    'crawler.middlewares.MyCustomDownloaderMiddleware': 543,
#      'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#      'crawler.middlewares.MyproxiesSpiderMiddleware':125
# }


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
