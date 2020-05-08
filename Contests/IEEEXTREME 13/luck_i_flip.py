import re, math, decimal, bisect
from collections import Counter
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

def chr_diff(a, b):
    ans = 0
    for i in range(len(a)):
        ans += 1 if a[i] == b[i] else 0
    return ans

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
# code goes here
n = iread()
bets = []
for i in range(n):
     bets.append(read())
length = 2 ** len(bets[0])
wins = Counter()
for i in range(length):
    correct = Counter()
    for b in bets:
        correct[b] = chr_diff(b, format(i, f"0{len(bets[0])}b"))
    l = correct.most_common(2)
    if l[0][1] != l[1][1]:
        wins[l[0][0]] += 1
print(wins.most_common()[-1][1])
    