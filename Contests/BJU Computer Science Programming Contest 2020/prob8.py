import re, math, decimal, bisect
from collections import deque
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    

def in_board(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

# code goes here
def moves__(sx, sy, dx, dy, d1, d2):
    visited = [[False for y in range(8)] for x in range(8)]
    q = deque([(sx, sy, 0)])

    while (True):
        s = q.pop()
        moves = s[2] + 1

        if s[0] == dx and s[1] == dy:
            return moves

        for d in [(-d1, -d2), (d1, -d2), (-d1, d2), (d1, d2), (-d2, -d1), (d2, -d1), (-d2, d1), (d2, d1)]:
            ddx = d[0] + s[0]
            ddy = d[1] + s[1]
            if in_board(ddx, ddy) and not visited[ddx][ddy]:
                visited[ddx][ddy] = True
                q.appendleft((ddx, ddy, moves))

n = iread()
for i in range(n):
    sx, sy, dx, dy = viread()

    if (abs(sx - dx) % 2 == 1 and abs(sy - dy) % 2 == 0) or (abs(sx - dx) % 2 == 0 and abs(sy - dy) % 2 == 1):
        print("KNIGHT")
        exit()

    csteps = moves__(sx, sy, dx, dy, 1, 3)
    ksteps = moves__(sx, sy, dx, dy, 1, 2)



    if csteps == ksteps:
        print("TIE")
    elif csteps < ksteps:
        print("CAMEL")
    else:
        print("KNIGHT")
