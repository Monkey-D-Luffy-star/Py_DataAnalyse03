import  numpy as np
import pandas as pd
import random

path = './starbucks_store_worldwide.csv'
# 读取星巴克数据
df = pd.read_csv(path)

gro = df['Brand'].groupby(by=[df['Country'],df['State/Province']])      # SeriesGroupBy类型
gro_count = gro.count()          # 得到一个Series，但是该Series有两个列组成index索引
print(gro_count.index)           # MultiIndex类型


df1 = pd.DataFrame(np.array([random.randint(1,10) for i in range(12)]).reshape((3,4)),index=list('123'),columns=list('wxyz'))
# 给索引赋值
df1.index = list('abc')

# reindex()方法,相当于从原DataFrame中取出对应的行，如果没有该行，则全赋值NaN，注意该方法有返回值
# df1 = df1.reindex(['a',1,2])
# print(df1)

# 设定某一列作为索引
df2 = df1.set_index('w')
print(df2.index)        # Int64Index([4, 10, 5], dtype='int64', name='w')
# drop参数的作用，仍然保留该列
df2 = df1.set_index('w',drop=False)
print(df2)

# index索引是可以重复的
print(df2['w'].unique())        # ndarray类型
print(df2.index.unique())       # 如下列
#    w  x  y   z
# w
# 9  9  6  5   3
# 5  5  3  5  10
# 5  5  6  3   5
# [9 5]
# Int64Index([9, 5], dtype='int64', name='w')

# 传入多列,注意返回值
df3 = df2.set_index(['w','x'])        # 可以传入多列形成复合索引
print(df3.index)