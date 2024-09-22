# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent
from urllib.request import HTTPHandler
#使用代理
from urllib.request import ProxyHandler
url = "http://www.baidu.com"
headers = {
    "User-Agent":UserAgent().chrome
}
request = Request(url, headers=headers)
hander = HTTPHandler()

#使用代理
#proxy = ProxyHandler({"http":"198.0.0.1:80"})
# opener = buile_opener(proxy)

opener = build_opener(hander)
response = opener.open(request)
print(response.read().decode())