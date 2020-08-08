import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = './books.csv'
df = pd.read_csv(path)
# print(df.info())

books = df[df['original_publication_year'] == df['original_publication_year']]

book_num = books.groupby(by='original_publication_year')['average_rating'].mean()


# 绘图
plt.figure(figsize=(20,8),dpi=80)

# 数据
x = book_num.index
y = book_num.values

# 绘图
plt.plot(range(len(x)),y)

# 展示
plt.show()
