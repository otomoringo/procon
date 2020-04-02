# -*- coding: utf-8 -*-

# 鏡餅の数
N = int(input())
# 違う大きさの鏡餅の集合
N_set = set()

# 重複排除しながら読み取る
for id in range(N):
    N_set.add(int(input()))

# 重複排除した鏡餅の個数
print(len(N_set))
