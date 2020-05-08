import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    n, m = viread()
    print(pow(1 << (m - 1), n, 10 ** 9 + 7))