import numpy as np
import pandas as pd

multi_df = pd.DataFrame(
    {'a': range(7), 'b': range(7, 0, -1), 'c': (['one' for i in range(4)] + ['two' for i in range(3)]),
     'd': ['h', 'i', 'j', 'k', 'l', 'm', 'n']})

df1 = multi_df.set_index(['c','d'])
print(df1)

# 常用操作
a = df1['a']
print(type(a))          # <class 'pandas.core.series.Series'>

# 输出a的切片
print(type(a['one']))   # <class 'pandas.core.series.Series'>
print(a['one']['i'])    # 1
# 另一种方式
print(a['one','i'])

# 另一种set_index方式
df2 = multi_df.set_index(['d','c'])
print(df2)
b = df2['a']
print(b)

# 如何取内层one对应的值呢？        交换level再取
print(b.swaplevel()['one'])
print(b.swaplevel()[['one']])


# 对于DataFrame（df2）,如何取到one对应的值呢
print(df2.swaplevel().loc['one',:])

print('-8'*50)
# 对于DataFrame（df2）,如何取到one,h对应的值呢
print(df2.swaplevel().loc['one',:].loc['k',:])