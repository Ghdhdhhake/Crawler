# Author:wjw
# Development date: 2024/9/26
from lxml import etree
import requests
from fake_useragent import UserAgent

url = "https://news.163.com/domestic/"
headers = {
    "User-Agent":UserAgent().chrome
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
contents = e.xpath('//h3/a/text()')
times = e.xpath('//div [@class="news_tag"]/span[1]/text()')
print(contents)
print(times)
# 对应打印
# for num in range(len(times)):
#     print(contents[num], ':', times[num])

# for time,content in zip(times, contents):
#     print(time, ':', content)
