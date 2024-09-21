# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request, urlopen
from urllib.parse import quote


url = "https://www.baidu.com/s?tn=25017023_2_dg&ch=5&ie=utf-8&word=[]".format(quote("尚学堂"))
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}
request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())