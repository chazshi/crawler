import re
# import requests
import time
import sched
import os
from concurrent.futures import ThreadPoolExecutor
__crawler_pool = ThreadPoolExecutor(30) #创建1个程池中，容纳线程个数为30个

__crawler_spiders = []  # 保存spider名
__crawler_time = 600    # 10分钟

#初始化sched模块的scheduler类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler ( time.time, time.sleep )

def __getSpiders():
    path = './crawler/spiders'
    dirs = os.listdir(path)
    for dir in dirs:
        # print(dir)
        # __dir_spider = re.search(r'(.+)_spider\.py', dir).group(1)
        # __crawler_spiders.append(__dir_spider)
        # print(__crawler_spiders)
        if re.search(r'(.+)_spider\.py', dir):
            __dir_spider = re.search(r'(.+)_spider\.py', dir).group(1)
            __crawler_spiders.append(__dir_spider)
    # print(__crawler_spiders)

def __crawl_task(__spider_name):
    # print(__spider_name)

    __task_os_cmd = 'scrapy crawl '
    __task_os_cmd += __spider_name
    # __task_os_cmd += ' --nolog'         # 不显示日志

    _time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    __task_os_cmd += ' -o ./log/%s_%s.json' % (_time, __spider_name)    # 输出到文件
    # __task_os_cmd += ' -t json'         # 输出文件后缀名

    # print(__task_os_cmd)

    # scrapy crawl anqing --nolog -o items.json
    os.system(__task_os_cmd)

    return True # 任务执行完毕可以返回一个值

def __crawl_task_done(__spider_name):
    print('task', __spider_name, 'done!')
#被周期性调度触发的函数
def func():
    # os.system("scrapy crawl News")
    for __spider_name in __crawler_spiders:
        __crawler_pool.submit(__crawl_task, __spider_name).add_done_callback(__crawl_task_done)
    # pass
def perform1(inc):
    schedule.enter(inc,0,perform1,(inc,))
    func()    # 需要周期执行的函数
def mymain():
    __getSpiders()  # 获取爬虫名
    schedule.enter(0,0,perform1,(__crawler_time,))

if __name__=="__main__":
    mymain()
    schedule.run()  # 开始运行，直到计划时间队列变成空为止



# __crawler_pool.submit(get_index,'http://www.xiaohuar.com/list-3-%s.html'% i ).add_done_callback(parse_index)

# if __name__ == '__main__':
#     main()