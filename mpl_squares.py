# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# 设置线条粗细
plt.plot(values,squares,linewidth=2)
# ~ 设置图表标题，并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("X",fontsize=14)
plt.ylabel("Y",fontsize=14)
# ~ 设置刻度标记的大小
plt.tick_params(axis="both",labelsize=14)

plt.show()