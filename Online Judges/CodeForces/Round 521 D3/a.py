from math import floor, ceil
for i in range(int(input())):
    a, b, n = [int(x) for x in input().split()]
    num_a = ceil(n / 2)
    num_b = floor(n / 2)
    print((a * num_a) - (b * num_b))