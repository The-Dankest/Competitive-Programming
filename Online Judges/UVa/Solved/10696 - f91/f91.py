def f91(x):
    if (x <= 100):
        return f91((f91(x + 11)))
    return x - 10


n = int(input())
while (n != 0):
    print("f91({0}) = {1}".format(n, f91(n)))
    n = int(input())