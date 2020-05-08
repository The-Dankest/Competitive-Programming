# BJU Bitwise Blitz 
# prob11.py

import math, re, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    total = 0
    index = 0
    for j in range(iread()):
        tweets = viread()
        total += tweets[index]
        index = (index + 2) % 3
    print(total)
