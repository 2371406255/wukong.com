from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  pymysql
import hashlib
import datetime
import requests
from lxml import etree
#-*-coding:utf8-*-
from lxml import etree
import xml.etree.ElementTree as etree

import requests

domain="https://www.50110.net/"

url="http://sh.qihoo.com/pc/home?sign=360_e39369d1&djsource=&refer_scene=so_7&uid=&tj_url=so_rec"
head={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
response=requests.get(url,headers=head)
# print(response.text)
text=response.content.decode('utf-8')
print(text)
# htmls=etree.HTML(nei)

# print(htmls)

#
# driver = webdriver.Chrome() #加载浏览器控件
# driver.set_window_size(850,1300)#窗口大小变化
# driver.get('http://sh.qihoo.com/pc/home?sign=360_e39369d1&djsource=&refer_scene=so_7&uid=&tj_url=so_rec')  #打开头条
#
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
#
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
#
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
# for i in range(60):
#     # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
#     driver.find_element_by_link_text('首页').send_keys(Keys.END)
#     driver.implicitly_wait(10)
# driver.refresh()
# time.sleep(1)
#
