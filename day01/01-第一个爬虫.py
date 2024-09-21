# Author:wjw
# Development date: 2024/9/21
from urllib.request import urlopen

url = "http://www.baidu.com"
#发送请求
response = urlopen(url)
#读取内容
info= response.read()
#打印内容
#print(info.decode())

print(response.getcode())#打印状态码
print(response.geturl())#打印真实url
print(response.info())#打印响应头
