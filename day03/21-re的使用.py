# Author:wjw
# Development date: 2024/9/24
import re

str1 = "I Study Python3.6 Everyday"
#print("___________match()_____________")
#打印首字母
m1 = re.match(r'I', str1)
m2 = re.match(r'\w', str1)
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'i', str1, re.I)
m6 = re.match(r'\S', str1)
m7 = re.match(r'Study', str1)#匹配不到，因为match是从左开始匹配


# print("___________search()_____________")
#打印Study
s1 = re.search(r'Study', str1)
s2 = re.search(r'S\w+', str1)

#打印Python3.6
s3 = re.search(r'P\w+.\d', str1)

print("___________findall()_____________")
#打印所有的字母y
f1 = re.findall(r'y', str1)
print(f1)
print("___________test_____________")
str2 = '<div><a herf="http://www.baidu.com">哔哩哔哩bilibili</a></div>'
t1 = re.findall(r'[\u4e00-\u9fff]\w+', str2)
t2 = re.findall(r'<a herf="http://www.baidu.com">(.+)</div>', str2)
t3 = re.findall(r'<a herf="(.+)">', str2)
print(t3)
print("___________sub()_____________")

su1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)
print(su1)