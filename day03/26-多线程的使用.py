# Author:wjw
# Development date: 2024/9/28
from threading import Thread
from queue import Queue
import requests
from fake_useragent import UserAgent
from lxml import etree

#爬虫类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().random
        }
        while self.url_queue.empty()==False:
            response = requests.get(self.url_queue.get(), headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)
#解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            div_contents = e.xpath('//div[@class="list_content"]//div[1]')
            with open("xiaohua.txt", 'a', encoding='utf-8') as f:
                for div in div_contents:
                    info = div.xpath('string(.)')
                    f.write(info + '\n')









if __name__ == '__main__':
    #存储url容器
    url_queue = Queue()
    #存储内容容器
    html_queue = Queue()

    base_url = 'https://tudouqu.com/index.php?p={}'
    for i in range(1, 4):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    crawl1_list = []
    #创建一个Crawl
    for i in range(0, 3):
        crawl1 = CrawlInfo(url_queue, html_queue)
        crawl1_list.append(crawl1)
        crawl1.start()
    parse_list = []
    for i in range(0, 3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()
    # for crawl1 in crawl1_list:
    #     crawl1.join()
    #
    # parse = ParseInfo(html_queue)
    # parse.start()