import re, math, decimal, bisect
def read(): return input()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
# code goes here
def wordkey(w):
    x = [0]
    for c in w[1:]:
        x.append(ord(w[0]) - ord(c))
    return tuple(x)

words = {}
for i in range(iread()):
    word = read()
    words[wordkey(word)] = word

print(*[words[wordkey(x)] for x in read().split()])