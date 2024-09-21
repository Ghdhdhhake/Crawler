# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent
args = {
    "wd":"尚学堂",
    "ie":"utf-8"
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))

headers={
    "User-Agent":UserAgent().random
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())