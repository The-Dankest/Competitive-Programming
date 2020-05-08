import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
s = read()
if s.count("1") != s.count("0"):
    print(1)
    print(s)
else:
    print(2)
    print(s[:n - 1], s[n - 1])
