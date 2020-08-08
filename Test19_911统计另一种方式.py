import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path='./911.csv'
df = pd.read_csv(path)

# 添加一列再进行分类的方法
temp_cate = df['title'].str.split(':').tolist()
cate = [i[0] for i in temp_cate]
cate_df = pd.DataFrame(np.array(cate).reshape((len(cate),1)),columns=['cate'])
# print(cate_df)
# 将创建的列拼接起来
df = df.join(cate_df)

# 分类统计
print(df.groupby(by='cate')['title'].count())