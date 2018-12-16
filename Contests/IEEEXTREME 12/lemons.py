import math
n, m, s = [int(x) for x in input().split()]
x = n
count = 0
while (x != 1):
    x = math.ceil(x / 2)
    count += 1
ans = (m * (n - 1)) + (count * s)
print(ans)