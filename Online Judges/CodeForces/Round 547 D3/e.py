import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
h, n = viread()
moves = viread()
mins = 0
for i in range(n):
    mins += 1
    h += moves[i]
    if h <= 0:
        print(moves)
