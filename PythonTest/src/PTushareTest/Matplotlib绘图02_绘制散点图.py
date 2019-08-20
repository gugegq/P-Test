'''
Created on 2019年8月5日

@author: qiao.gu
'''
# 技术要点：plt.scatter(x,y)

from matplotlib import pyplot as plt
from matplotlib import font_manager as ftm
from PyInstaller.building.templates import bundleexetmplt

# 参数设置
x_3=[11,21,30,14,5,16,7,18,9,10,11,15,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
x_10=[21,32,13,24,15,6,17,28,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

y_3=range(1,32)
y_10=range(51,81)

# 字体设置，可以显示中文字符
my_font=ftm.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)

# 绘制图形
plt.scatter(x_3, y_3)
plt.scatter(x_10,y_10)
# 展示图形
plt.show()