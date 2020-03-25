# -*- coding: utf-8 -*-
N, A, B= map(int, input().split())

# 1以上N以下の整数のリスト
target_list = range(1, N+1)
print(target_list)

# nについて各桁の総和のリストを返す
def sum_each_digit(n):
    return sum(list(map(int,str(n))))

digit_sum_list = list(map(sum_each_digit,target_list))
print(digit_sum_list)

# A以上B以下はTrue、それ以外はFalse
def A_more_B_less(x, a, b):
    return (a <= x and x <= b) if True else False

bool_list = list(map(lambda x: A_more_B_less(x, A, B), digit_sum_list))
print(bool_list)

# 総和を求める
combined = [x * y for (x, y) in zip(target_list, bool_list)]
print(combined)

ans = sum(combined)
print(ans)
