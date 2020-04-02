# -*- coding: utf-8 -*-
import math
import sys

# N:枚数
# Y:合計金額
N, Y = list(map(int, input().split()))

# 合計金額を10000で割った数値が1万円の最大枚数
max_x = math.floor(Y / 10000)

# xの値を設定（最大枚数から0まで繰り返す）
for i in range(max_x + 1):
    x = max_x - i
    # 5000円札の最大枚数
    max_y = N - x
    for j in range(max_y + 1):
        y = max_y - j
        z = N - x - y
        otoshidama = 10000 * x + 5000 * y + 1000 * z
        if(otoshidama == Y):
            print('{} {} {}'.format(x,y,z))
            sys.exit()

print('{} {} {}'.format(-1,-1,-1))
