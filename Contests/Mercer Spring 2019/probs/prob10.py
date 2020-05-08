# BJU Bitwise Blitz 
# prob10.py

import math, re, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
edges = []
edges.append([[None, None, None]]*90)
edges.append([[None, None, None]]*90)
ans = [10, 90]
eidx = 0
digs = [int(x) for x in "0123456789"]
i = 0
for d in digs:
    for d2 in digs:
        if d == d2:
            continue
        edges[eidx][i] = [d, d2, 1]
        edges[eidx+1][1] = [d, d2, 0]
        i += 1

#for i in range(2):
#    for p in range(90):
#        print(edges[i][p])

for foo in range(2, 500):
    for e in edges[eidx]:
        a, b, w = e
        if a < b:
            for d in digs[b-1::-1]:
                # going up, search down
                if d == a: continue
                edges[eidx ^ 1][9*b+d][2] += w
        else:
            for d in digs[b:]:
                # going down, search up
                if d == a: continue
                edges[eidx ^ 1][9*b+d-1][2] += w
    i = 0
    s = 0
    #print(edges)
    for i in range(90):
    edges[eidx][i][2] = 0
    edges [eidx ^ 1][i][2] %= 10**9 + 7
    s += edges[eidx ^ 1][i][2]
    #print(edges)
    ans.append(s)
    eidx ^= 1

n = iread()
for i in range(n):
    print(ans[iread() - 1])
