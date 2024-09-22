# Author:wjw
# Development date: 2024/9/23
#未完成
from urllib.request import Request, urlopen, HTTPCookieProcessor, build_opener
from fake_useragent import UserAgent
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar

#登录
#保存cookie文件
def get_cookie():
    login_url = "https://www.sxt.cn/login?redirect=https://www.sxt.cn/"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    from_data = {
        "user": "15129667951",
        "password": "white814"
    }
    f_data = urlencode(from_data).encode()
    request = Request(login_url, headers=headers, data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)

def use_cookie():
    info_url = "https://www.sxt.cn/setting.html"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load("cookie.txt", ignore_discard=True, ignore_expires=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().deocde())



if __name__ == '__main__':
    #get_cookie()
    use_cookie()

