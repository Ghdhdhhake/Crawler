# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
#from urllib.request import HTTPCookieProcessor

#登陆网页
login_url = "https://www.sxt.cn/index/login/getphone"
headers = {
    "User-Agent":UserAgent().chrome
}
from_data = {
    "user":"15129667951",
    "password":"white814"
}
f_data = urlencode(from_data).encode()
request = Request(login_url, data=f_data)
response = urlopen(request)
#保存
# hander = HTTPCookieProcessor()
# opener = build_opener(hander)
# response = opener.open(request)

print(response.read().decode())

#访问页面
info_url = "https://www.sxt.cn/setting.html"
request = Request(info_url, headers=headers)
response = urlopen(request)

#保存
#response = opener.open(request)

print(response.read().decode())