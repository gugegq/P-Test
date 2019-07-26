'''
Created on 2019年7月3日

@author: qiao.gu
'''
import asyncio
from pyppeteer import launch
import time
import pandas as pd
import html
from numpy.ma.core import get_data
from tushare import fund
from asyncio import tasks
# from stock_util import get_all_codes

async def create_page():
    browser = await launch()
    page = browser.newPage()
    return browser, page
async def close_page(browser):
    await browser.close()
async def callurl_and_getdata(page, fund):
    print('fund:'+fund)
    url = 'https://xueqiu.com'
    df = pd.DataFrame(columns=['AA','AB','AC','AD','AE','AF'])
    await page.goto(url)
    html = page.content()
    df = get_data(html, df)
    print('df:'+df)
    
if __name__ == '__main__':
#     fundlist = get_all_codes()
    loop = asyncio.get_event_loop()
    browser, page = loop.run_until_complete(create_page())
    start_time = time.time() 
    print(start_time)
    tasks = [asyncio.ensure_future(callurl_and_getdata(page, fund)) for fund in 'abcdefghijklmn']
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(close_page(browser))
    print(time.time() - start_time)
    
    
    
#     start_time = time.time()
#     print(start_time)
#     count = 0
#     for fund in fundlist:
#         print(fund)
# #         df = pd.dataframes(column=['CG','DQJ','ZDF','CJL','ZSZ','NCZJ'])
#         await page.goto(url)
#         html = await page.content()
# #         df = get_data(html, df)
# #         print(df)
#     await browser.close()
#     print(time.time() - start_time)
#     
# if __name__ == '__main__':
# #     fundlist = get_all_codes()
# #     asyncio.get_event_loop().run_until_complete(callurl_and_getdata(fundlist[:50]))