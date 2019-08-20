'''
Created on 2019年8月20日

@author: qiao.gu
'''

import pandas as pd
import numpy as np
from numpy import size
import matplotlib.pyplot as plt
from pandas import Series
from _operator import index
from IPython import display
from pandas.core.frame import DataFrame


path='D:/TuShare/20190820_600570.xlsx'

# Numpy基础练习
# n1=np.random.randint(0,100,size=4)
# print(n1)
# n2=np.random.randint(0,100,size=(4,5))
# print(n2)
# n3=np.random.randint(0,100,size=(5,4))
# print(n3)
# print(n1*n3)
# print(np.dot(n1,n2))

# a1=np.ones((2,3))
# a2=np.array(2)
# print(a1+a2)

# n=np.random.randint(0,100,size=50)
# print(n)
# print('------------------------------')
# print(np.sort(n))
# n2=np.sort(n)
# print('------------------------------')
# print(np.partition(n,5))
# print('------------------------------')
# print(np.partition(n2,-5))
# print(n2)

# Series基础练习
# plt.imread('./test.jpg')
# nd = np.array([1,4,5,2,3,7])
# print(nd)
# s=Series(nd)
# print('-------------------')
# print(s)
# print('-------------------')
# s.index=list('abcdef')
# print(s)
# print('----------多维度---------')
# n2=np.random.randint(0,100,size=(4,6))
# print(n2)
# print('-------------------')
# n3=Series(n2,index=list('a'+np.random.randn(0,20,size=(4,6))))
# print(n3)
# print('-------------------')
# s=Series(np.random.randint(0,100,size=10),index=list('abcdefghih'))
# print(s)
# print(s.loc['g':])
# print(s.tail(4))
# df=pd.read_excel(path)
# print(df)
# date=df['date']
# print(date.head(10))
# s1=Series([1,2,3,4],index=list('abcd'))
# s2=Series([100,99,98,97],index=list('opqr'))
# print(s1)
# print('-------------------')
# print(s2)
# print('-------------------')
# print(s1+s2)

# DataFrame基础练习
df=pd.read_excel(path)
# print(df)
s=df.tail(5)
print(s)
s.index('ABCDE')
print(s)
# s.loc['D':]
print('----------------------------------------------------------')
# # display(df.index,df.column,df.values)
# s=DataFrame({'age':[10,21,31,43,55],'height':[178,188,164,168,177],'sex':['Female','Male','Male','Female','Male'],
#              'price':np.random.randint(0,10000,size=5)})
# # s.index=[1,2,3,4,5]
# print(s)
# s2=s['age']
# print(s2)
# print(s.ix)