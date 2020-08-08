import pandas as pd
import numpy as np
from pymongo import MongoClient

# numpy的loadtxt方法不仅仅可以读csv文件
# path = './haha.txt'
# t = np.loadtxt(path,delimiter=',',dtype=int)
# print(t)
# 读取csv文件，不需要指定','或者其他符号作为分隔符，也不需要指定读取后的类型
# 但是第一行不会被赋值索引
t = pd.read_csv('./youtube_video_data/GB_video_data_numbers.csv')
print(t)
# client = MongoClient(host='localhost',port=27017)
# collection = client['douban']['tv1']
# data = list(collection.find())