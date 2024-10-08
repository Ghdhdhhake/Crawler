# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"
for i in range(10):
    headers = {
        "User-Agent" : UserAgent().chrome
    }
    url = base_url.format(i * 20)
    request = Request(url, headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    if info == "" or info is None:
        break
    i += 1
