n, a, b = [x for x in input().split()]
n = int(n)
a = int(a, 2)
b = int(b, 2)
ag = 0
while (a != 0):
    a = a >> 1
    ag = ag ^ a
bg = 0
while (b != 0):
    b = b >> 1
    bg = bg ^ b
print(ag , bg)