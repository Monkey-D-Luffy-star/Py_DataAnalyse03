import numpy as np
import pandas as pd

path = './starbucks_store_worldwide.csv'
# 读取星巴克数据
df = pd.read_csv(path)
print(df.info())
# print(df.info())

# 对读取到的数据分类,得到一个对象,该对象可迭代
# 并且拆分后每个都是一个元组，元组第一个数据是分组属性，第二个是该分类下的DataFrame
grouped = df.groupby('Country')
# print(type(grouped))        # DataFrameGroupBy

# for i,j in df:
#     print('*'*100)
#     print(i)
#     print('-'*100)
#     print(j)

# 统计每个分类的数据，得到每个国家中对应属性的总数
print(grouped.count())          # 返回DataFrame类型
# 统计其中一个属性的总数['Brand']
country_count = grouped['Brand'].count()
print(country_count['US'])  # 美国13608家
print(country_count['CN'])  # 中国2734家

# 统计中国每个省份星巴克数量
CN_starbucks = df[df['Country'] == 'CN']
CN_grouped = CN_starbucks.groupby('State/Province')
print(CN_grouped['Brand'].count())

# 聚合操作，count(),mean(),median(),min(),max(),std(),var()

# 按照多个列进行分组
# 首先df['Brand']已经取出了Brand列，那么在by=后面必须使用df['Country']形式
# 不能直接写列名，因为df['Brand']中不含Country列
# 如果前面是df.groupby，那么后面by=可以直接跟属性列列表['Country','State/Province']
# 如果我想返回DataFrame类型，那么df[['Brand']],必须这种写法
gro = df['Brand'].groupby(by=[df['Country'],df['State/Province']])      # SeriesGroupBy类型
print(gro.count())          # 得到一个Series，但是该Series有两个列组成index索引

