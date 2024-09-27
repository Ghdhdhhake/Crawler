# Author:wjw
# Development date: 2024/9/27
from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent
url = "https://www.89ip.cn/"
headers = {
    "User-Agent":UserAgent().random
}
response = requests.get(url, headers=headers)
doc = pq(response.text)
ip = doc('')
port = doc('')
types = doc('')
# ??????????????
# trs = doc('#ip_list tr')
# for num in range(1, len(trs))):
#     ip = trs.eq(num).find('td').eq(1).text()
#     prot =  trs.eq(num).find('td').eq(2).text()
#     types =  trs.eq(num).find('td').eq(5).text()
#     print(ip, ":", port, "-------", type)