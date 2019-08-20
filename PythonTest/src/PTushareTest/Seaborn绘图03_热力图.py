'''
Created on 2019年8月6日

@author: qiao.gu
'''
'''
Annotated heatmaps
================================
'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#通过加载sns自带数据库中的数据（具体数据可以不关心）
flights_long=sns.load_dataset("flights")
flights=flights_long.pivot("month","year","passengers")

# 使用每个单元格中的数据值绘制一个热力图heatmap
sns.heatmap(flights,annot=True,fmt="d",linewidths=.5)
plt.show()