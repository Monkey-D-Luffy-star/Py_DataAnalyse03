import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

path = './books.csv'
df = pd.read_csv(path)
# print(df.head(1))
# print(df.info())

# 统计不同年份书的数量
# books = df[df['original_publication_year'] == df['original_publication_year']]
# 或者如下写法
books = df[pd.notnull(df['original_publication_year'])]

book_num = books.groupby(by='original_publication_year')['title'].count().sort_values(ascending=False)
print(book_num,type(book_num))

# book_num[:50]         # 这里会报错，不知道为什么？index must be monotonic increasing or decreasing
# 只要index是int或者float类型就会出现这个问题
# 下面测试book_num.index不单调也可以的啊，为什么会报这个错？
# 换一种方式取前50
book_num = book_num.head(50)

y = book_num.values
x = book_num.index

# 293个年份
plt.figure(figsize=(20,12),dpi=80)

plt.barh(range(len(x)),y)

# 设置x,y轴显示
plt.yticks(range(len(x)),x)
plt.xticks(range(0,max(book_num.values)+50,50))

plt.show()


# Test
s = pd.Series([0,1,2,3,4,5,6,7,8,9],index=[3,1,4,5,2,7,8,3,5,2])
print(s,type(s))
s = s[:3]
print(s)