import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
l = viread()
swapped = True
moves = []
for i in range(1, n + 1):
    # find i
    index = l.index(i)
    if index + 1 != i:
        moves.append((i, l[i - 1]))
        l[index], l[i - 1] = l[i - 1], l[index]
print(len(moves))
for m in moves:
    print(m[0], m[1])
