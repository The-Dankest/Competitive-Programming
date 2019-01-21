def f(x):
    x = str(x)
    s = 0
    for c in x:
        s += int(c)
    return s

def g(x):
    while(x > 9):
        x = f(x)
    return x

n = int(input().strip())
while (n != 0):
    print(g(n))
    n = int(input().strip())