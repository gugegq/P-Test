'''
Created on 2019年7月3日

@author: qiao.gu
'''
# -*- coding: utf-8 -*-

import xlwt
import xlrd

class ExcelPrintPipeline(object):
    def __init__(self):
        self.f = xlwt.Workbook()  # 创建工作薄
        self.sheet1 = self.f.add_sheet(u'种子资源', cell_overwrite_ok=True)
        self.rowsTitle = [u'标题', u'影片名称', u'导演', u'影片演员', u'语言', u'影片类型', u'影片地区', u'更新时间', u'影片状态', u'上映日期', u'剧情介绍', u'影片地址']  # 创建标题
        for i in range(0, len(self.rowsTitle)):
            # 最后一个参数设置样式
            self.sheet1.write(0, i, self.rowsTitle[i], self.set_style('Times new Roman', 220, True))
        # Excel保存位置
        self.f.save('D:/torrent_movie.xls')

    def open_spider(self, spider):
        print("开始输出xlsx文件")

    def process_item(self, item, spider):
        data = xlrd.open_workbook('D:/torrent_movie.xls')  # 打开Excel文件
        table = data.sheets()[0]  # 通过索引顺序获取table，因为初始化时只创建了一个table，因此索引值为0
        rowCount = table.nrows  # 获取行数   ，下次从这一行开始
        data = []
        # 拼装成一个列表
        # data.append(rowCount + m)  # 为每条添加序号
        data.append(item['torrent_title'])
        data.append(item["torrent_name"])
        data.append(item["torrent_director"])
        data.append(item["torrent_actor"])
        data.append(item['torrent_language'])
        data.append(item["torrent_type"])
        data.append(item["torrent_region"])
        data.append(item["torrent_update_time"])
        data.append(item['torrent_status'])
        data.append(item["torrent_show_time"])
        data.append(item["torrent_introduction"])
        data.append(item["torrent_url"])

        for i in range(len(data)):
            self.sheet1.write(rowCount, i, data[i])  # 写入数据到execl中
        self.f.save('D:/torrent_movie.xls')
        return item

    def close_spider(self, spider):
        self.f.save('D:/torrent_movie.xls')
        print("结束输出xlsx文件")

    #该函数设置字体样式
    def set_style(self,name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style