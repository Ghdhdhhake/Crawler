# Author:wjw
# Development date: 2024/9/25
import requests
from fake_useragent import UserAgent
import re
url = "https://www.gushicimingju.com/xiehouyu/#:~:text=%E6%AD%87%E5%90%8E%E8%AF%AD%E6%98%AF%E4%B8%80%E7%A7%8D%E7%94%A8%E6%9D%A5"

headers = {
    "User-Agent":UserAgent().random
}
#构造请求
response = requests.get(url, headers=headers)
info = response.text
infos = re.findall(r'<div class="content">\s*(.+)\s*<\span>', info)
#打印
with open('content.txt', 'w', encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n\n\n")