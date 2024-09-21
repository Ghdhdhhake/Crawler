# Author:wjw
# Development date: 2024/9/21
#not run normal
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from fake_useragent import UserAgent

#get: 字典 > str > byte
url = "https://www.sxt.cn/login?redirect=https://www.sxt.cn/setting.html"
form_date = {
    "user": "15129667951",
    "password": "white814"
}
headers = {
    "User-Agent": UserAgent().chrome
}

f_date = urlencode(form_date)
request = Request(url, data=f_date.encode(), headers=headers)
response = urlopen(request)
print(response.read().decode())
# <script>alert('必填项不能为空'); history.go(-1);</script>