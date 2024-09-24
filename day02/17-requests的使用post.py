# Author:wjw
# Development date: 2024/9/24
import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent":UserAgent().chrome
}
url = "https://www.sxt.cn/index/login/getphone"
params = {
        "user": "15129667951",
        "password": "white814"
    }
response = requests.get(url, headers=headers, data=params)
print(response.text)