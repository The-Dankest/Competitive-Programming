import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
while True:
    line = viread()
    if line[0] == 0:
        break
    pairs = 0
    for i in range(line[0] - 2):
        if line[i + 1] > line[i + 2]:
            pairs += 1
    print("{} rogue pairs".format(pairs))
