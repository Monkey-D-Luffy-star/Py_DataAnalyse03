import numpy as np
import pandas as pd


# # 创建时间数组DatetimeIndex，start接起始时间，end接结束时间，freq接频率，D表示一天
# d1 = pd.date_range(start='20191220',end='20200213',freq='D')
# print(d1)
#
# # 也可以使用10D表示间隔十天
# d1 = pd.date_range(start='20191220',end='20200213',freq='10D')
# print(d1)
#
# # periods参数指示数组中产生多少数据，M表示月，B表示工作日，H小时，T或min每分钟
# d1 = pd.date_range(start='20191220',periods=3,freq='M')
# print(d1)

# t1 = np.eye(3)
# print(type(t1))

t1 = np.array([1,2,3,1,2,3,3,2,1])
temp = np.where(t1==1)
print(temp)
t1 = np.arange(1,15).reshape((2,7))
print(np.sum(t1,axis=1))


