#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')        
    for j in range(i-1):
        print('*',end=' ')
    print('*',end='')
    for j in range(5-i):
        print(' ',end='') 
    print('')

