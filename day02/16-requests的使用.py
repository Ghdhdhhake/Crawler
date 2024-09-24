# Author:wjw
# Development date: 2024/9/24
import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent":UserAgent().chrome
}
url = "https://www.baidu.com/s"
params = {
    "wd":"哔哩哔哩"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)