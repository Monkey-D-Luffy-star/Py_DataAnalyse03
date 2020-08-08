import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path='./911.csv'
df = pd.read_csv(path)

# print(df.head(1))
# print(df.info())

# 统计每种事故发生的次数
# 首先统计事故类型有多少种
title_list = df['title'].str.split(':').tolist()
# print(title_list[:100])

# 输出灾难类型
disasters = list(set([i[0] for i in title_list]))
# print(disasters)

# 创建一个DataFrame
statistics = pd.DataFrame(np.zeros((df.shape[0],len(disasters))),columns=disasters)

# 遍历进行赋值
for i in disasters:
    statistics[i][df['title'].str.contains(i)] = 1
    pass
# 另一种速度贼慢的方式
for i in range(df.shape[0]):
    statistics.loc[i][title_list[i][0]] = 1
    pass


# 赋值完后查看
print(statistics.sum(axis=0))
