#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a="Hello World"
temp=[]
b=""

for i in range(len(a)):
    if (ord(a[i])>=97)&(ord(a[i])<=122):
        temp.append(chr(ord(a[i])-32))
    else:
        temp.append(a[i])
for i in temp:
    b+=i
a=b
print(a)