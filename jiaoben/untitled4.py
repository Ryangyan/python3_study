# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:09:55 2021

@author: 56957
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:46:28 2021

@author: 56957
"""

temp = input().split('\n')
n = 2 * int(temp[0])
duiyuan = temp[1].split(' ')
duiyuan = list(map(int, duiyuan))
duiyuan.sort()
total = sum(duiyuan)
half = int(total / 2)

dp = [[False for i in range(half + 1)] for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = True
for i in range(1, half + 1):
    dp[0][i] = False

for i in range(1,n+1):
    for j in range(i,0,-1):
        for k in range(1, half + 1):
            # print(i, j, k)
            if k >= duiyuan[i-1] and dp[j-1][k-duiyuan[i-1]]:
                dp[j][k] = True

for i in range(2, n+1):
    for j in range(1, half+1):
        if dp[i-1][j]:
            dp[i][j] = True

for i in range(half,0,-1):
    if dp[n][i]:
        print(abs(total - 2*i),end='')
        break;