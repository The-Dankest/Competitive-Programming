def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return x * (y / gcd(x, y))

a, b, c = [int(x) for x in input().split()]
if (lcm(a, b) <= c):
    print("yes")
else:
    print("no")
    