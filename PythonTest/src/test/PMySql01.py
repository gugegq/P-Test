'''
Created on 2019年7月19日

@author: qiao.gu
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# #初步查询
# import pymysql
# 
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "K@ppy213", "test", charset='utf8' )
# 
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
# 
# # 使用execute方法执行SQL语句
# # cursor.execute("SELECT VERSION()")
# cursor.execute("SELECT * from user")
# 
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# 
# print("Database version : %s " % data)
# 
# # 关闭数据库连接
# db.close()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "K@ppy213", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 创建数据库表
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# 插入数据
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

cursor.execute(sql)

# 关闭数据库连接
db.close()