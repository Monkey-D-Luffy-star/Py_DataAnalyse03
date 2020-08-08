import numpy as np
import pandas as pd



# # 创建DataFrame
# t = pd.DataFrame(np.arange(1,13).reshape(3,4))
# print(t)
#
# # 传入index和columns参数
# t = pd.DataFrame(np.arange(1,13).reshape((3,4)),index=['a','b','c'],columns=list('wxyz'))
# print(t)
#
# 传入字典创建DataFrame
d1 = {'name':['zhangsan','lisi'],'age':[23,24],'prop':['计算机','中医学']}
t = pd.DataFrame(d1,index=['z','l'],columns=[1,2,3])      # 传入其他的columns会创建为NaN
print(t)

# # 第二种字典传入方式
# d2 = [{'name':'wangjian','age':22,'prop':'计算机'},{'name':'zhumengya','age':23,'prop':'计算机'},{'haha':'haha'}]
# t = pd.DataFrame(d2)
# print(t)
#
# # DataFrame的属性
# print(t.shape)      # DataFrame的形状（行，列）
# print(t.index)      # 行键
print(t.columns,type(t.columns))    # 列键
# print(t.values)     # 包含的值，是ndarray类型
# print(t.dtypes)     # 类型
# print(t.ndim)       # 维度

csvinfo = pd.read_csv('./youtube_video_data/GBvideos.csv')
# print(csvinfo)
# print(type(csvinfo))
# print(csvinfo.shape)

# 显示头几行
print(csvinfo.head(2))
print('-*'*50)
print(csvinfo.tail(2))

# 展示DataFrame的info
print(csvinfo.info())

# DataFrame的describe函数，用于展示DataFrame的数字列统计信息
print(csvinfo.describe())

# 对DataFrame进行排序
csvinfo = csvinfo.sort_values(by='likes',ascending=False)
print(csvinfo.head(5))