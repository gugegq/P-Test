'''
Created on 2019年8月6日

@author: qiao.gu
'''
import tushare as ts
import pandas as pd
import time
import os
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

Date_Today = time.strftime("%Y%m%d")
print(Date_Today)

# 连接数据库
engine = create_engine('mysql://root:K@ppy213@localhost/sjfx?charset=utf8')

path='D:/TuShare/'+Date_Today+'_History_恒生电子.xlsx'

# 获取恒生电子历史数据
df=ts.get_hist_data('600570')
# # 保存数据
# df.to_excel(path)
# 写入数据库
df.to_sql('History_HSDZ',engine,if_exists='append')

