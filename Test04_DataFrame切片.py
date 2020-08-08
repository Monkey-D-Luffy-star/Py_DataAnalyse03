import pandas as pd
import numpy as np

t0 = pd.read_csv('./youtube_video_data/GBvideos.csv')

# 输出前20行，结果为DataFrame
# 注意不能直接写t0[2],里面不能直接写数字,直接写会被认为是取列,写数字的集合也不行，除非列中有该索引，否则报错
print(t0[:20])

# 同时对行列操作，当只选取一列时，结果类型为Series
# 先取行和先取列结果是一样的
# 总结：取行就使用':数字'的形式，取列就使用字符串索引
print(t0[:20]['video_id'])
print(t0['date'][:3])

t1 = pd.DataFrame(np.arange(1,16).reshape((3,5)),index=list('abc'),columns=[1,2,3,4,5])
print(t1)

# 直接写数字被认为是取列操作,结果为Series类型,可以使用['a','b']来取行
# 但是当行索引为数字时使用[,,]传入的方式会报错，除非改写成[:2]这种形式
print(t1[1][['a','b']])

print('-*'*40)
# 总结：取多列，传入列表用逗号隔开[,,]，只能用这种形式
# 注意，行只能用[:2]和非数字的列表这种形式
# print(t1[[3,4]])

# 不容易混淆更方便的方法,使用loc定位
print(t1.loc[['a','b'],[1,2]])
# 注意这种情况，a,b,c行全会被选出来
print(t1.loc['a':'c',[1,2]])

# 使用数字进行切片
print(t1.iloc[1,2])
# 和numpy有所区别，这里取出的是第1,2行和2,3列的交叉部分，其余和numpy数字切片一样操作
# 可直接进行赋值操作，可直接赋值np.nan不用类型转换，DataFrame会自动进行转换
t1.iloc[[1,2],[2,3]] = 30
print(t1)


