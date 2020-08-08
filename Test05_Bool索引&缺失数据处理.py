import pandas as pd
import numpy as np
import random

t = pd.read_csv('./DogName.csv')
# print(t)

# 布尔索引
print(t[t['count']>100])
# print(t[80<t['count']<100])                   # 不能像Python一样连写
# &表示与，必须要用括号括起来，|表示或运算
# 单独80<t['count']是一个Bool型的Series序列
print(t[(80<t['count']) & (t['count']<100)])

print('--'*50)
# 输出每只狗狗名字的长度
print(t['DogName'].str.len(),type(t['DogName'].str.len()))

# t['DogName'].str.很多方法
# 其余较常用的有.str.split('切割符号')，用于将字符串转换成列表，最后输出的形式的Series
# .str.split('切割符号').tolist，可以加个整个Series的value部分转换为一个大列表，其中嵌套小列表


# 缺失数据处理
t1 = pd.DataFrame(np.array([random.randint(1,10) for i in range(15)]).reshape((3,5)),index=list('abc'),columns=list('vwxyz'))
# 定位数据并赋值nan
t1.loc['b':,'v':'w'] = np.nan
print(t1)
# 下面这样赋值会报警告SettingWithCopyWarning，而且内容并未修改，要使用loc或者iloc进行修改
# t1[:1]['z'] = np.nan
# print(t1)


# 判断是否含有nan
print(pd.isnull(t1))
# 判断不是null
print(pd.notnull(t1))

# 只要含有nan就删除行，当how = 'all'时表示该行全为nan时才删除
# inplace属性表示是否进行原地操作，即直接对t1进行修改
print(t1.dropna(axis=0,how='any'))

# 将t1中的nan值填充为20
# t1.fillna(20,inplace=True)
# print(t1)

# 输出t1的均值，注意pandas求均值时和numpy有所不同，pandas求均值会自动将nan数据过滤掉，求方差等亦是
# print(t1.mean())
# 将nan值用均值填充
# t1.fillna(t1.mean(),inplace=True)
# print(t1)
# 单独对某一字段进行nan填充
t1['v'].fillna(t1['v'].mean(),inplace=True)
print(t1)

