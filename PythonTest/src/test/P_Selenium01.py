'''
Created on 2019年7月18日

@author: qiao.gu
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.maximize_window()
browser.minimize_window()
browser.close()