import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
_sum = 0
for i in range(n - 2):
    _sum += (i + 2) * (i + 3)
print(_sum)