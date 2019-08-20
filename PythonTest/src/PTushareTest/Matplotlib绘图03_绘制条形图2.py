'''
Created on 2019年8月5日

@author: qiao.gu
'''
# 技术要点：plt.scatter(x,y)

from matplotlib import pyplot as plt
from matplotlib import font_manager as ftm
from matplotlib.font_manager import FontProperties
from scipy.spatial.transform import rotation

# 参数设置
x=["哪吒","战狼2","复仇者联盟4","冰与火之歌","疯狂速递","速度与激情"]
y=[11,25,67,101,32,56]

# 字体设置，可以显示中文字符
my_font=ftm.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)

# 绘制图形
plt.bar(range(len(x)),y)
# 设置字符串到X轴
plt.xticks(range(len(x)), x, FontProperties=my_font,rotation=-45)
# 展示图形
plt.show()