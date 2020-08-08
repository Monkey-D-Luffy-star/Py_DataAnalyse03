import pandas as pd
import numpy as np
import random

path = './movies.csv'
df = pd.read_csv(path)
# 输出DataFrame基本信息
print(df.info())

# 输出第一行查看格式
print(df.head(1))

# 获取平均分
print(df['Rating'].mean())

# 获取导演总人数
print(len(set(df['Director'].tolist())))
# 另一种方法
print(len(df['Director'].unique()))

# 获取演员的人数
actor_list = df['Actors'].str.split(',').tolist()
print(actor_list)
# print(actor_list)               # 大链表嵌套小列表
# 记住下面这种双重循环展开的方式
actors = [i for j in actor_list for i in j]
# 另一种展开方式
# 这里actor_list由于有些含有nan值，导致不是矩形，直接传入ndarray会报错，正常情况下可有如下写法
# actors = np.array(actor_list).flatten()
print(actors)
# 输出演员人数
print(len(set(actors)))

# 电影时长的最大最小值
print(df['Runtime (Minutes)'].max())    # 191分钟
print(df['Runtime (Minutes)'].min())    # 66分钟
print(df['Runtime (Minutes)'].argmax())    # Index索引：828
print(df['Runtime (Minutes)'].argmin())    # Index索引：793
print(df['Runtime (Minutes)'].median())     # 中位数111分钟
