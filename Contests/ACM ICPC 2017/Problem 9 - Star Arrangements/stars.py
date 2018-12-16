while (True):
    try:
        n = int(input().strip())
        print("{0}:".format(n))
        for i in range(1, int(n / 2) + 1):
            row1 = i + 1
            row2 = i
            if ((n / (row1 + row2)) % 1 == 0.0 or ((n - row1) / (row1 + row2)) % 1 == 0.0):
                print(" {0},{1}".format(row1, row2))
            if ((n / row1) % 1 == 0.0):
                print(" {0},{1}".format(row1, row1))
    except EOFError:
        break