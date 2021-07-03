# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:33:19 2021

@author: 56957
"""
import numpy as np
temp = input().split('\n')
list1 = temp[0].split(',')
temp[1] = temp[1].replace(',','->')
list2 = temp[1].split('->')
list1 = list(map(int,list1))
list2 = list(map(int,list2))
dict1 = {}
i = 0
while(i < len(list2)):
    if list2[i] in dict1:
        dict1[list2[i]].append(list2[i+1])
    else:
        dict1[list2[i]] = [list2[i+1]]
    i += 2

result = list(np.zeros(len(list1)))
result = list(map(int,result))
flag = list(np.zeros(len(list1)))
flag = list(map(int,result))
temp = 0
while(0 in flag):
    for j in range(len(list1)):
        if flag[j] == 1:
            continue
        else:
            if j not in dict1:
                temp += list1[j]
                result[j] = temp
                flag[j] = 1
            else:
                panduan = 1
                for k in dict1[j]:
                    panduan = panduan & flag[k]
                if k == 1:
                    temp += list1[j]
                    result[j] = temp
                    flag[j] = 1
                else:
                    continue
print(result)