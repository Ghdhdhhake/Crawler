# Author:wjw
# Development date: 2024/9/24
# Author:wjw
# Development date: 2024/9/24
import requests
from fake_useragent import UserAgent

#保存登录
session = requests.session()
headers = {
    "User-Agent":UserAgent().chrome
}
login_url = "https://www.sxt.cn/index/login/getphone"
params = {
        "user": "15129667951",
        "password": "white814"
    }
response = session.post(login_url, headers=headers, data=params)

info_url = "https://www.sxt.cn/setting.html"
resp = session.get(info_url, headers=headers)
print(resp.text)