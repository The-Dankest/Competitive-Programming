from math import ceil
n, k = [int(x) for x in input().split()]
ans = ceil((n * 2) / k) + ceil((n * 5) / k) + ceil((n * 8) / k)
print(ans)