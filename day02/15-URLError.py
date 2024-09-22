# Author:wjw
# Development date: 2024/9/23
from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = "https://www.git.com"
try:
    headers = {
        "User-Agent":UserAgent().chrome
    }
    req = Request(url, headers=headers)
    resp = urlopen(url, timeout=1)
    print(resp.read().decode())
except URLError as e:
    if(len(e.args)) == 0:
        print(e.code)
    else:
        print(e.args[0])
print("End")


