import pandas as pd
import random
import string
# 创建Series
t0 = pd.Series([1,2,3,4])
print(t0)
print(type(t0))

t1 = pd.Series([random.randint(2,9) for i in range(5)],index=list('abcde'))
print(t1)

# 通过字典创建
t_dict = {'猪头':24,'haha':True,23:'OK'}
t2 = pd.Series(t_dict)
print(t2)

_t = {string.ascii_uppercase[i]:i for i in range(0,11)}
t3 = pd.Series(_t)
# 修改之后要重新赋值
t3 = t3.astype(float)
print(t3)

# 取出t3中的部分数据和NaN
t4 = pd.Series(_t,index=list(string.ascii_uppercase[5:15]))
print(t4)
print(t4['G'])
# 这种写法会将index也写出来
print(t4[0:1])
print(t4[:2])


print('-*'*50)
# 取index
print(type(t4.index))
print(list(t4.index))           # 强制类型转换为列表

# 取value
print(t4.values)
print(type(t4.values))

# pandas的where方法和numpy的where方法有所区别
# numpy的where方法用于修改数组，t.where(t>10,20)将t中所有大于10的数修改为20
# pandas的where方法用于筛选，t.where(t>10,20)，将t中所有大于10的数不做改变，其余数改称20