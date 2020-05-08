import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here

n = iread()
peeps = sorted(viread())
ans = 1
dp = []
for i in range(len(peeps) - 1):
    dp.append(peeps[i + 1] - peeps[i])
for i in range(dp)