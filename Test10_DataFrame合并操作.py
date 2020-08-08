import numpy as np
import pandas as pd

# DataFrame的拼接，横着拼接使用join
# 自然连接使用merge

df1 = pd.DataFrame(np.ones((3,4)),index=list('abc'),columns=list('xyzw'))
print(df1)

df2 = pd.DataFrame(np.zeros((3,2)),index=list('bcd'),columns=list('12'))
print(df2)

# df1 = df1.join(df2)
# print(df1)

df3 = pd.DataFrame(np.arange(1,9).reshape((2,4)),index=list('12'),columns=list('xyzw'))
print(df3)

# 按照列x进行自然连接,默认是inner
# df1 = df1.merge(df3,on='x')
# print(df1)

# 按照列x进行右连接，how=left为左连接，outer为外连接
df1 = df1.merge(df3,on='x',how='right')
# df1按x列，df3按y列进行右连接
df1 = df1.merge(df3,left_on='x',right_on='y',how='right')

