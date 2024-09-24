# Author:wjw
# Development date: 2024/9/24
import requests
from fake_useragent import UserAgent


url = "https://httpbin.org/get"
headers = {
    "User-Agent":UserAgent().chrome
}
proxies = {
    "http":"3847539:fjiae893@127.0.0.1:7890"
}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)