for i in range(int(input())):
    h, m, s = [int(x) for x in input().split(":")]
    if (m % 10 == 0 and s == 0):
        print(0)
    else:
        print((10 - (m % 10)) * 60 - s)
