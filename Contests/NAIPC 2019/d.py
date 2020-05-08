import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def vfread(): return [float(_) for _ in input().strip().split()]
def vsread(): return input().strip().split()

def SUM(n):
    return n * (n + 1) // 2

# code goes here
for i in range(iread()):
    p, q, n = viread()
    print((p % q) * (SUM(n) % (q * n)))
    