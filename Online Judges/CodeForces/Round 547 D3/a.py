import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
a, b = viread()
moves = 0
if (b % a != 0):
    print(-1)
    exit()
c = b // a
while (c % 2 == 0):
    moves += 1
    c //= 2
while (c % 3 == 0):
    moves += 1
    c //= 3
if c != 1:
    print(-1)
else:
    print(moves)