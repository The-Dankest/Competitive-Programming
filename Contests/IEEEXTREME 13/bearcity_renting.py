import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n, m = viread()
edges = {}
edges_used = set()
for i in range(n):
    edges[i] = []
for i in range(m):
    a, b, w = viread()
    edges[a - 1].append((w, b - 1))
    edges[b - 1].append((w, a - 1))
for v in range(n):
    edges[v].sort()
    if len(edges[v]) == 1 or edges[v][0][0] != edges[v][1][0]:
        edges_used.add((min(v, edges[v][0][1]), max(v, edges[v][0][1]), edges[v][0][0]))
print(len(edges_used))