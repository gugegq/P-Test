'''
Created on 2019年7月2日

@author: qiao.gu
'''

# -*- coding: utf-8 -*-
import os
import re
import sys
import ssl
import json
import time
import xlwt
import urllib
import urllib2
import shutil


from pyExcelerator import *

# 取消证书验证
context = ssl._create_unverified_context()

# 每页动态数量（最多60条）
perPage = 60;

# 文件存放路径
filePath = 'd:/Reptilian/health/xxxx/'

# 记录条数
count = 1

# 创建工作簿
import xlwt 

filePath = 'd:/Reptilian/health/xxxx/'

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('sheet1')

# 爬虫基础地址，某站热门热门动态接口，打开网页通过开发者工具分析得来
xxxxUrl = 'https://api.xxxxx.com/social/v2/timeline/hot?startPage={}&perPage='+ str(perPage) +'&lastId=5aee63773c549f58fa1c3bb1'


# 请求头定义
headers = {
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept':'text/html,application/xhtml+xml,application/xml;\
        q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

# 获取用户信息
def getUserInfo(page):
    url = xxxxUrl.format(str(page))
    print(('爬取内容(每次' + str(perPage) + '条)地址：' + url).decode('utf-8').encode('gbk'))
    req = urllib2.Request(url, headers = headers)
    resp = urllib2.urlopen(req, context = context)
    result = resp.read().decode('utf-8');
    jsonData = json.loads(result)
    if jsonData['ok']:
        # 接口调用成功
        users = jsonData['data']
    else:
        # 接口调用失败
        print('接口调用失败！'.decode('utf-8').encode('gbk'));
        return
    global count
    if len(users) > 0:
        for user in users:
            if (getCorrectName(user['author']['username']) == ''):
                break
            # 拿上传图片列表
            if ('images' in user.keys()):
                imgs = user['images']
                imgNum = len(imgs)
                if imgNum > 1:
                    worksheet.write_merge(count, count + imgNum - 1, 0, 0, getCorrectName(user['author']['username']))
                    worksheet.write_merge(count, count + imgNum - 1 , 1, 1, user['author']['gender'])
                    worksheet.write_merge(count, count + imgNum - 1 , 2, 2, user['author']['avatar'])
                    worksheet.write_merge(count, count + imgNum - 1, 4, 4, getCorrectDate(str(user['created'])))
                    worksheet.write_merge(count, count + imgNum - 1, 5, 5, getCorrectContent(user['content']))
                    for img in imgs:
                        worksheet.write (count, 3, img)
                        count += 1
                elif imgNum == 1:
                    worksheet.write(count, 0, getCorrectName(user['author']['username']))
                    worksheet.write(count, 1, user['author']['gender'])
                    worksheet.write(count, 2, user['author']['avatar'])
                    worksheet.write(count, 3, imgs[0]) 
                    worksheet.write(count, 4, getCorrectDate(str(user['created'])))
                    worksheet.write(count, 5, getCorrectContent(user['content']))
                    count += 1
                else:
                    worksheet.write(count, 0, getCorrectName(user['author']['username']))
                    worksheet.write(count, 1, user['author']['gender'])
                    worksheet.write(count, 2, user['author']['avatar'])
                    worksheet.write(count, 3, user['photo']) 
                    worksheet.write(count, 4, getCorrectDate(str(user['created'])))
                    worksheet.write(count, 5, getCorrectContent(user['content']))
                    count += 1
            else:
                worksheet.write(count, 0, getCorrectName(user['author']['username']))
                worksheet.write(count, 1, user['author']['gender'])
                worksheet.write(count, 2, user['author']['avatar'])
                worksheet.write(count, 3, '') 
                worksheet.write(count, 4, getCorrectDate(str(user['created'])))
                worksheet.write(count, 5, getCorrectContent(user['content']))
                count += 1

# 创建制定目录
def mkDir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExist = os.path.exists(path)
    
    if not isExist:
        os.makedirs(path)
    else:
        print('目录已存在，不需要重复创建！'.decode('utf-8').encode('gbk'))

# 验证名称是否合法(只保留中文和英文)
def getCorrectName(name):
    temp = re.sub(r'([\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])', '', name)
    #re.sub(r'(\\-)', '', temp)
    return temp

# 替换动态中的特殊字符
def getCorrectContent(content):
    return re.sub(r'#|xxxx|XXXX|@', '', content)

# 获取正确格式时间
def getCorrectDate(time):
    t =  re.sub(r'T', ' ', time)
    return re.sub(r'(.[0-9]*Z$)', '', t)


if __name__ == '__main__':
    # 创建目录
    mkDir(filePath)
    # 创建表格头部
    worksheet.write (0, 0, '用户昵称'.decode('utf-8').encode('gbk').decode('gbk'))
    worksheet.write (0, 1, '用户性别'.decode('utf-8').encode('gbk').decode('gbk'))
    worksheet.write (0, 2, '用户头像'.decode('utf-8').encode('gbk').decode('gbk'))
    worksheet.write (0, 3, '用户上传图片'.decode('utf-8').encode('gbk').decode('gbk'))
    worksheet.write (0, 4, '动态创建时间'.decode('utf-8').encode('gbk').decode('gbk'))
    worksheet.write (0, 5, '用户动态'.decode('utf-8').encode('gbk').decode('gbk'))
    # 获取用户信息并写入表格
    for i in range(0, 200):
        getUserInfo(i)
    # 保存xls文件
    workbook.save(filePath + 'content.xls')