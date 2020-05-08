a, d, m = [int(x) for x in input().split()]
green, purple, black = [int(x) for x in input().split()]
print("YES") if (green - a >= 0 and purple + green - a - d >= 0 and black + purple + green - a - d - m >= 0) else print("NO")