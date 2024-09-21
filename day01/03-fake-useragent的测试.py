# Author:wjw
# Development date: 2024/9/21
from fake_useragent import UserAgent

#创建对象
ua = UserAgent()

print(ua.chrome)
print(ua.firefox)
print(ua.edge)
print(ua.safari)