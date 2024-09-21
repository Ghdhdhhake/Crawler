# Author:wjw
# Development date: 2024/9/21
from urllib.request import urlopen
from urllib.request import Request
from random import choice


url = "http://www.baidu.com"
#动态UA
user_agents = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1']

headers = { "User-Agent":choice(user_agents) }

request = Request(url, headers=headers)
print(request.get_header("User-agent"))#查看请求头