import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMKAI.TTF')

path = './starbucks_store_worldwide.csv'
# 读取星巴克数据
df = pd.read_csv(path)

# 取出中国数据
CN_df = df[df['Country']=='CN']

# 按城市分组,计数，排序，选前四十
CN_df_city = CN_df.groupby(by='City')['Brand'].count().sort_values(ascending=False)[:41]
# print(CN_df_city)

# 绘画布
plt.figure(figsize=(20,12),dpi=80)

# 准备数据
y = CN_df_city.values
x = CN_df_city.index

plt.barh(range(len(x)),y,height=0.4)

# 显示y轴坐标
plt.yticks(range(len(x)),x,fontproperties=myfont,size=14)

# 展示
plt.show()