'''
Created on 2019年8月5日

@author: qiao.gu
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from pandas import Series,DataFrame

# 在线获取数据
df=sns.load_dataset("flights")
print(df.head())
sns.heatmap(df)