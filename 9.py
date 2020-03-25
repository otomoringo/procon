# -*- coding: utf-8 -*-

# 入力文字列
S = input()

dream   = "dream"
dreamer = "dreamer"
erase   = "erase"
eraser  = "eraser" 

ans = "YES"

while(ans == "YES"):
    if(S[len(dream):] == dream or S[len(dream):] == ""):
        print(S[len(dream):])
        print(S[:len(dream)])
        S = S[:len(dream)]
    elif(S[len(dreamer):] == dreamer or S[len(dreamer):] == ""):
        print(S[len(dreamer):])
        print(S[:len(dreamer)])
        S = S[:len(dreamer)]
    elif(S[len(erase):] == erase or S[len(erase):] == ""):
        print(S[len(erase):])
        print(S[:len(erase)])
        S = S[:len(erase)]
    elif(S[len(eraser):] == eraser or S[len(eraser):] == ""):
        print(S[len(eraser):])
        print(S[:len(eraser)])
        S = S[:len(eraser)]
    else:
        ans = "NO"

print(ans)
