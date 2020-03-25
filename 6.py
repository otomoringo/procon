# -*- coding: utf-8 -*-
N = input()
list_N = list(map(int, input().split()))
list_N.sort(reverse=True)

alice_sum = sum(list_N[::2])
bob_sum = sum(list_N[1::2])

ans = alice_sum - bob_sum

print(ans)
