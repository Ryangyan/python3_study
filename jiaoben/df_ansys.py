#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:56:51 2020

@author: yangan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sheet = pd.read_csv('/Users/yangan/Desktop/college.csv',encoding='utf-8')
print("————————————————打印前5行————————————————")
print(sheet.head(5))
print("————————————————打印行索引————————————————")
print(sheet.index)
print("————————————————打印列索引————————————————")
print(sheet.columns)
print("————————————————有多少所大学————————————————")
print(sheet.shape[0])
print("————————————————国际竞争力最大值———————————————")
print(max(sheet['国际竞争力']))
print("————————————————综合分数平均值———————————————")
print(np.mean(sheet['综合分数']))
print("————————————————找出湖南大学———————————————")
print((sheet.loc[sheet['学校名称']=='湖南大学',['学校名称','综合分数','排名']]))
print("————————————————找出每个地点大学数———————————————")
strlist=[]
intlist=[]
for i in sheet['地点']:
    if i not in strlist:
        strlist.append(i)
        temp=len(sheet.loc[sheet['地点']==i])
        intlist.append(temp)
        print('在%s有%d所前100大学'%(i,temp))
print("————————————————排序后———————————————")        
mydict=dict(zip(strlist,intlist))
a = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
x=[]
y=[]
for i in a:
    x.append(i[0])
    y.append(i[1])
    print('在%s有%d所前100大学'%(i[0],i[1]))

plt.bar(x[:10],y[:10])
plt.xticks(size = 10)
plt.yticks(range(0,max(y)+1,1),size = 10)
plt.title('前100大学数城市排行（前10名）')
plt.savefig('/Users/yangan/Desktop/bar.png', dpi=300) #指定分辨率保存