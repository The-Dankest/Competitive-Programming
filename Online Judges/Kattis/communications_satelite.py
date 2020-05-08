from math import sqrt

class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

n = int(input())
edges = []
sat = []
for i in range(n):
    x1, y1, r1 = [int(_) for _ in input().split()]
    for j in range(len(sat)):
        x2, y2, r2 = sat[j]
        d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) - r1 - r2
        e = (i, j, d)
        edges.append(e)
    sat.append((x1, y1, r1))

ds = UFDS(n)
weight = 0
edges.sort(key=lambda a: a[2])
while ds.numdisjoint != 1:
    a, b, w = edges.pop(0)
    if ds.find(a) != ds.find(b):
        ds.union(a, b)
        weight += w

print(f"{float(weight):.09}")
