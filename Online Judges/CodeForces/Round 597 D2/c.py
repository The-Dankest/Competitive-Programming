import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

def comb(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 3
    if x == 4:
        return 5
    else:
        pass

# code goes here
mod = 10 ** 9 + 7
ans = 1
word = read()
letters = set(word)
if "m" in letters or "w" in letters:
    print(0)
else:
    for x in re.findall(r"[u]+", word):
        ans *= comb(len(x))
    for x in re.findall(r"[n]+", word):
        ans *= comb(len(x))
    
    # split word into consecutive sequences of letters
    #for group in word
    print(ans % mod)