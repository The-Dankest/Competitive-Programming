import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

n = iread()
string = list(read())
ans = 0
chars = ['R', 'B', 'G']
for i in range(n - 1):
    if string[i] == string[i + 1]:
        ans += 1
        if (i + 2 < n):
            for c in chars:
                if string[i] != c and string[i + 2] != c:
                    string[i + 1] = c
        else:
            for c in chars:
                if string[i] != c:
                    string[i + 1] = c
print(ans)
print("".join(string))
            