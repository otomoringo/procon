# -*- coding: utf-8 -*-

# 入力文字列
S = input()
rev_S = S[::-1]

dream   = "dream"
dreamer = "dreamer"
erase   = "erase"
eraser  = "eraser" 

# 後ろから3番目の文字で判別可能
rev_str_dict = {
    'e':dream[::-1]
    ,'m':dreamer[::-1]
    ,'a':erase[::-1]
    ,'s':eraser[::-1]
}

print(rev_S)
print(rev_str_dict)

# 3文字目の文字から辞書を取得
target_word = rev_str_dict[rev_S[2]]
cut_word = rev_S[:len(target_word)]
if()


if len(rev_S) == 0:
    print("YES")
elif len(rev_S) < len(target_word):
    print("NO")
