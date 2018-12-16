import math
n, x, y = [int(x) for x in input().split()]
z = math.sqrt((x ** 2) + (y ** 2))
for i in range(n):
    n = int(input())
    if (n <= z):
        print("DA")
    else:
        print("NE")
