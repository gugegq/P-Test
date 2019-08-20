# -*- coding: utf-8 -*-

'''
Created on 2019年7月31日

@author: qiao.gu
'''

from matplotlib import pyplot as plt, font_manager
import random
from scipy.spatial.transform import rotation
from scipy.constants.constants import alpha
from cProfile import label
from matplotlib.font_manager import FontProperties
from django.core.management import color
# 设置字体，显示中文字符
my_font=font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

x=range(2,26,2)
y=[15,13,14,5,17,20,25,26,24,22,18,15]
z=[19,21,31,5,12,11,16,13,17,21,15,18]

# 设置图片大小
plt.figure(figsize=(20,8), dpi=80)

# 绘制图形
plt.plot(x,y,label="自己",color="red")
plt.plot(x,z,label="别人",color="green")
# 调整X&Y轴的刻度密集度
# 绘制X轴的刻度,旋转字符串，rotation=90
_xtick_labels=["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,FontProperties=my_font)
# plt.xticks(range(2,26),rotation=-45)
# 取X轴步长操作
# plt.xticks(x[::3])
# 绘制Y轴的刻度
plt.yticks(range(min(y), max(y)+1))
# 添加XY轴描述信息，且调用引用中文
plt.xlabel("年龄",FontProperties=my_font)
plt.ylabel("温度 单位('C)",FontProperties=my_font)
plt.title("从10点到12点每分钟的气温变化情况",FontProperties=my_font)

# 绘制网格，并设置透明度
plt.grid(alpha=0.3)
# 添加图例，只能用prop来添加字体
plt.legend(prop=my_font)

# 保存图形
# plt.savefig("./t1.svg")
# 展示图形
plt.show()

# 参考资料
# matplotlib.org官方文档 