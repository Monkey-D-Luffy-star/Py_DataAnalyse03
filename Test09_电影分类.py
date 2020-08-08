import numpy as np
import pandas as pd

path = './movies.csv'
# 读出数据
df = pd.read_csv(path)

# print(df['Genre'])
# 首先统计所有电影分类数
genre_list = df['Genre'].str.split(',').tolist()
genre = list(set([i for j in genre_list for i in j]))
print(genre)

# 统计数据
# 首先创建一个二维数组
sta = pd.DataFrame(np.zeros((df.shape[0],len(genre))),columns=genre,dtype=int)

# 遍历df统计信息,下面这种写法写麻烦了
# k = 0
# for i in genre_list:
#     for j in i:
#         sta.loc[k][j] = 1
#         pass
#     k += 1
#     pass

# 另一种统计方法，这里genre_list[i]仍然为列表，是一行多列
for i in range(df.shape[0]):
    sta.loc[i,genre_list[i]] = 1
    pass


# 已经遍历完成
print(sta)
# 统计各列之和即为某类电影共多少部，下面方法较麻烦
# for i in genre:
#     print('{}：{}部'.format(i, sta[i].sum()))

# 另一种方法
print(sta.sum(axis=0))