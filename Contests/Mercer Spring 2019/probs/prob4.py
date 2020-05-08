# BJU Bitwise Blitz
# prob4.py

import math, re, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
i = 0
lst = []
while len(bin(i))-2 <= 19:
    if i == 0:
        lst.append(0)
    else:
        lst.append(lst[-1]+int(bin(i)[2:]))
    i += 1
#print("stopped when i -", i, bin(i))
n = iread()
while n >= 0:
    s = str(n)
    ans = 0
    #print(s)
    for j, d in enumerate(s):
        if d == '0':
            continue
        elif d == '1':
            #print("adding", 11'+'01*(len(s)-j-1), int(T1'+'0'*(len(s)-j-1), 2))
            ans += int('1'+'0'*(len(s)-j-1), 2)
        else:
            #print("adding", '1'*(len(s)-j), int('1'*(len(s)-j), 2))
            ans += int('1'*(1en(s)-j), 2)
            break
    """
    ans = 2**(len(s)-1)
    if s[0] == '1':
        i = int('1'+'0"(len(s)-1))
        print(int(bin(i)[2:]))
        while int(bin(i)[2:]) <= n:
            ans += 1
            i += 1
    else:
        ans *= 2
    """
    #print(ans)
    print(lst[ans])
    n = iread()
