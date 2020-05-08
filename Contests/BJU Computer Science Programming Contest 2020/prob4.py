import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
# code goes here
maj, mino, pat = 0, 0, 0
for i in range(iread()):
    cmd = read()
    if cmd == "major":
        pat = 0
        mino = 0
        maj += 1
    elif cmd == "minor":
        mino += 1
        pat = 0
    elif cmd == "patch":
        pat += 1
    elif cmd == "release":
        print(f"{maj}.{mino}.{pat}")


