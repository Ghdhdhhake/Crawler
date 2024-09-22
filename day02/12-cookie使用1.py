# Author:wjw
# Development date: 2024/9/21
from urllib.request import Request,urlopen
from fake_useragent import UserAgent

url = "https://www.sxt.cn/user/userinfo"
headers = {
    "User-Agent":UserAgent().chrome,
    "Cookie":"53gid2=13955067798002; 53gid0=13955067798002; 53gid1=13955067798002; 53revisit=1726904204796; visitor_type=old; 53kf_72904441_from_host=www.sxt.cn; 53kf_72904441_keyword=https%3A%2F%2Fcn.bing.com%2F; uuid_53kf_72904441=cd71da998460699f8f54b37ba627243d; 53kf_72904441_land_page=https%253A%252F%252Fwww.sxt.cn%252F; kf_72904441_land_page_ok=1; 53uvid=1; onliner_zdfq72904441=0; PHPSESSID=rpiobkp2m8c9mm5ste174s2jq7; my_acc_reauto_time=1726932898278; tfstk=fNUq9_G-GZQqzDQ65juZTn-GG4gxWqXCuPMss5ViGxDDlE9g45VD5cXY18ogdJFXlA1xjIUzLFTfHiFM7VgGd9_CRSFjWVXCNWhpJxhTZADYG233MV3GFQTGAwPYLLwQor0Ga4cZ1n0iIxfrqXMkofYmsLfref0MommmqUcI6fxDmRVlafHoshD_Ny49UficO8oL8DvN1mD3ixV_1zYtmnFmUjGYzjzqNSjkSF4rgmz1Ae8BWmZg9DUb1N8-lWrorfzOthkZYl4jrrXl-0ngjkiaVKfbKRPuBqalsnD3c-guokRMS7uqUcGqDKWrKrFuJ4m5-6Puy-NYz5OGSbwIESUm7wfKuqDmzbU1eEDaql4jDVpcQAUzZrqN4dvtZtR3WoJMbmc-av1PaMCN_CgkUS9vXhnAMbkCimx9Xmc-av1PahKtD-hrdsmc.; user=a%3A3%3A%7Bs%3A2%3A%22id%22%3Bs%3A32%3A%225647b5783fafc8886f85a06c227523d4%22%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2215129667951%22%3Bs%3A5%3A%22local%22%3Bi%3A0%3B%7D; token=4D4A6DCB975F4624C96E0A6068CD388A"
}
request = Request(url, headers=headers)

response = urlopen(request)
print(response.read().decode())