import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here

def rv(s, v=0):
    if s == "":
        return ""
    elif s == "A" or s == "E" or s == "I" or s == "O" or s == "U":
        return v + 1, rv(s[1:])
    else:
        return s[0] + rv(s[1:], v)

words = {}

for i in range(iread()):
    word = read()
    rv_word = rv(word)
    if word not in words:
        words[rv_word] = [(word, ]