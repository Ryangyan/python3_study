# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:16:48 2021

@author: 56957
"""

a = input().split(' ')
zongjin = float(a[0])
nianli = float(a[1])
fenqi = int(a[2])

yueli = nianli / 12
benxi = yueli * pow(1 + yueli, fenqi) * zongjin / (pow(1 + yueli, fenqi) - 1)
benjin = []
temp = zongjin / fenqi
for i in range(fenqi):
    benjin.append(temp + (zongjin - temp * i) * yueli)

print("%.2f %.2f %.2f\n%.2f %.2f %.2f"
      %(benxi,benxi,benxi*fenqi,benjin[0],benjin[1],sum(benjin)),end='')