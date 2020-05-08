import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
j = iread()
n = [int(_) for _ in read()]
count = 0
for i in range(len(n)):
    if n[i] % 2 == 0:
        count += i + 1
print(count)