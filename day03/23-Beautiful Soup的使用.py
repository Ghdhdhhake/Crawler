# Author:wjw
# Development date: 2024/9/25
#http://beautifulsoup.readthedocs.jo/zh_CN/latest
from bs4 import BeautifulSoup
from bs4.element import Comment
str = '''
<title id="title">百度知道</title>
<div class='info' float='left'>Welcome to PAPA</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a herf='www.baidu.com'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str, "lxml")

print(soup.title)
print(soup.div)
print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a['herf'])
print(soup.div.string)
print(soup.div.text)


print(soup.strong.string)
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())
else:
    print(soup.strong.text)#不解析

print("------------find_all()-----------")
print(soup.find_all('title'))
print(soup.find_all(id='title'))
print(soup.find_all(class_='info'))
print(soup.find_all(attrs={'float':'left'}))
print(soup.find_all('div', attrs={'float':'left'}))


print("-------------css()-----------------------")
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('.info'))
print(soup.select('div span'))
print(soup.select('div>span'))
print(soup.select('div')[1].select('a'))
print(soup.select('title')[0].text)