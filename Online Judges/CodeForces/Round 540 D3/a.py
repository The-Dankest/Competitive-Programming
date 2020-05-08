import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here

for i in range(iread()):
    n, a, b = viread()
    print(min((n // 2) * b if n % 2 == 0 else (n // 2) * b + a, (n * a)))
