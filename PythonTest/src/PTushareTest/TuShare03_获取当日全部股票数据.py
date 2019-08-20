'''
Created on 2019年8月2日

@author: qiao.gu
'''
import tushare as ts
import pandas as pd
import time
import os
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

Date_Today=time.strftime("%Y%m%d")
print(Date_Today)
path='D:/TuShare/'+Date_Today+'_today_all.xlsx'

# 获取当日所有股票数据
df=ts.get_today_all()

# 连接数据库
engine = create_engine('mysql://root:K@ppy213@localhost/sjfx?charset=utf8')

# 保存数据
df.to_excel(path)
# 写入数据库
df.to_sql('Today_All_Data',engine,if_exists='append')

# def get_all_data():
#     df=ts.get_today_all()
#     print(df)
#     
# if __name__ == '__main__':
#     get_all_data()