# -*- coding: utf-8 -*-
N = input()
A = map(int, input().split())

A_ = map(lambda x: x**2, list(A))
print(list(A_))

# A = list(A)
# count = 0
# flag = True

# while flag:
#     l = []
#     for element in A:
#         if element%2 == 1:
#             flag = False
#             count -= 1
#             break
#         l.append(element/2)
#     A = l
#     count += 1

# print(count)
