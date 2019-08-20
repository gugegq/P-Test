'''
Created on 2019年7月5日

@author: qiao.gu
'''
import asyncio
from pyppeteer import launch
async def main():
    browser = await launch(headless =False)
    page = await browser.newPage()
    await page.goto('https://www.jianshu.com')
    await page.screenshot({'page':'jianshu.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())