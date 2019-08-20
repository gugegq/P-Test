from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import baostock as bs
import tushare as ts
import pandas as pd

def download_data(date):
    bs.login()
    # 获取指定日期的指数、股票数据
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    for code in stock_df["code"]:
        print("Downloading :" + code)
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    bs.logout()
    data_df.to_csv("D:/TuShareP/demo_assignDayData.csv", encoding="gbk", index=False)
    engine = create_engine('mysql://root:H@ppy214@localhost/sjfx?charset=utf8')
    # 存入数据库
    data_df.to_sql('Bstock_Today_All', engine)
    # print(data_df)

if __name__ == '__main__':
    # 获取指定日期全部股票的日K线数据
    download_data("2019-08-19")