import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

path = './starbucks_store_worldwide.csv'
# 读取星巴克数据
df = pd.read_csv(path)

# 按国家进行分类,并求和计算每个国家有多少家
df = df['Brand'].groupby(by=df['Country']).count()
# 按数字进行排序，ascending=False则降序，并取前十
df = df.sort_values(ascending=False)[:10]

# 对这些数据进行绘图
plt.figure(figsize=(20,8),dpi=80)

x = df.index
y = df.values

# 绘图
plt.bar(range(10),y,width=0.3)

# 设置x坐标
plt.xticks(range(10),x,size=16)
plt.yticks(range(0,14001,500))
plt.title('星巴克数量最多的前十个国家',fontproperties=myfont,size=18)

# 展示
plt.show()

