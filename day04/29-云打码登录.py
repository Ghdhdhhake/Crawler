# Author:wjw
# Development date: 2024/10/9
import requests
from fake_useragent import UserAgent
from day04.yzm_util import get_cpde
def get_image():
    img_url = ''
    response = requests.get(img_url, headers=headers)
    with open('yzm.ipg', 'wb') as f:
        f.write(response.content)
    code = get_code('yzm.jpg')
    return code

if __name__ == '__main__':
    index_url = 'https://console.jfbym.com/login/?domain=https%3A%2F%2Fwww.jfbym.com'
    headers = {
        "User-Agent":UserAgent().random
    }
    response = requests.get(index_url, headers=headers)
    code = get_image()