# Author:wjw
# Development date: 2024/10/13
import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'https://www.farmer.com.cn/2024/09/27/99966008.html'
headers = {
    "User-Agent":UserAgent().random
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
title = e.xpath('//h1//text()')
content = e.xpath('//div[@class="textList"]/p/span/text()')
img_urls = e.xpath('//div[@class="textList"]/p/span/img/@src')