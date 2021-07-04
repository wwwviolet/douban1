#-*- coding = utf-8 -*-
#@Time : 2021/6/5 22:01
#@Author : lqw
#@File : test.py
#@software : PyCharm

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup


# response = urllib.request.urlopen("https://www.baidu.com/")
#
# print(response.read().decode("utf-8"))



'''
#转换二进制信息
#获取一个post请求
import urllib.parse     #解析器
#使用urllib模拟浏览器真实发出一次请求
data = bytes(urllib.parse.urlencode({}),encoding="utf-8")   #转为二进制格式
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))
'''

'''
#获取一个get请求
response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))
'''

'''
#超时处理
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)        #timeout多少秒内有响应
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("timeout!")
'''


#getheaders读取多个，getheader读取一个
response = urllib.request.urlopen("http://httpbin.org/get")
print(response.status)
print(response.getheader('Date'))


#模拟浏览器发起信息
# url = "http://www.douban.com"
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"}
# data = bytes(urllib.parse.urlencode({"world":"name"}),encoding="utf-8") #返回到from
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# # req = urllib.request.Request(url=url,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
# print(type(data))

# url = "http://www.baidu.com"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"}
# req = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
# douban = response.read().decode("utf-8")
# bs = BeautifulSoup(douban,"html.parser")
# print(douban)

# f = open("baidu.html","w",encoding="utf-8")
# f.write(douban)
# f.close()


