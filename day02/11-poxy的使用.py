# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = "https://httpbin.org/get"
headers = {
    "User-Agent":UserAgent().chrome
}
request = Request(url, headers=headers)
# handler = ProxyHandler({"http":"username:password@ip:port"})
# handler = ProxyHandler({"http":"3847539:fjiae893@127.0.0.1:7890"})

handler = ProxyHandler({"http":"127.0.0.1:7890"})
opener = build_opener()
response = opener.open(request)
print(response.read())


