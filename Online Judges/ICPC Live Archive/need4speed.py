while True:
    try:
        n, t = [int(x) for x in input().strip().split()]
        d = 0
        s = 0
        offset = 0.0
        for i in range(n):
            dist_speed = [int(x) for x in input().strip().split()]
            d += dist_speed[0]
            s += dist_speed[1]
        offset = (d / (t * n)) - s
        print("{0:.9f}".format(offset))
    except EOFError:
        break