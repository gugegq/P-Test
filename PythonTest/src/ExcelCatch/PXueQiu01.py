'''
Created on 2019年7月5日

@author: qiao.gu
'''

'''
Created on 2019年7月3日

@author: qiao.gu
'''
from pyppeteer import launch
import time

def create_page(url):
    browser = launch()
    page = browser.newPage()
    page.goto(url)
    
if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    print(time.time() - start_time)
    url1 = 'https://xueqiu.com'
    create_page(url1)