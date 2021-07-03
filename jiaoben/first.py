#!/usr/bin/env python3
# -*- coding: utf-8 -*-

total_sum=0
for i in range(1,11):
    temp_sum=1
    for j in range(1,i+1):
        temp_sum*=j
    total_sum+=temp_sum
print(total_sum)