import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

path = './movies.csv'
# 读出数据
df = pd.read_csv(path)
runtime = df['Runtime (Minutes)'].tolist()
rating = df['Rating'].tolist()

# # 均为1000条数据
# print(len(runtime),len(rating))

# 画布
plt.figure(figsize=(20,8),dpi=80)

# 大致分布在60--200,划分成14列
numbins = 16


# 绘图
# plt.hist(runtime,range(60,201,10))
plt.hist(rating,range=(1,9),bins=numbins)
#
# # 设置x轴
x = [i/2 for i in range(2,19)]
plt.xticks(x)
plt.yticks(range(0,251,25))


# # 设置标题
plt.title('电影评分分布图',fontproperties=myfont,size=18)
plt.xlabel('分数（10分制）',fontproperties=myfont,size=16)
plt.ylabel('电影数（部）',fontproperties=myfont,size=16)
#
# # 展示
plt.show()