# -*- coding: utf-8 -*-

'''
Created on 2018年11月22日

@author: qiao.gu
'''

from selenium import webdriver
import time

dr = webdriver.Chrome()

url = 'http://www.baidu.com'
print (url)
dr.get(url)


dr.close()
time.sleep(5)

dr2 = webdriver.Firefox()

url = 'https://www.sina.com.cn'
print (url)
dr2.get(url)
time.sleep(5)
dr2.close()