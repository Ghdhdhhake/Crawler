# Author:wjw
# Development date: 2024/9/29
import base64
import requests

with open('H:\Git and Code\Crawler\day04\dis.jpg', 'rb') as f:
    b = base64.b64encode(f.read()).decode()  ## 图片二进制流base64字符串
def verify():
    url = "http://api.jfbym.com/api/YmServer/customApi"
    data = {
        ## 关于参数,一般来说有3个;不同类型id可能有不同的参数个数和参数名,找客服获取
        "token": "ZgJK3Y9fIXaoLavUlHuTrLU3X-vmSb1isKhcScOEQnM",
        "type": "10110",
        "image": b,
    }
    _headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("Post", url, headers=_headers, json=data).json()
    print(response)

if __name__ == '__main__':
    verify()

