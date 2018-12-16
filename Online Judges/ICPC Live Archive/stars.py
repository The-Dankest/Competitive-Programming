from math import ceil
while True:
    try:
        n = int(input())
        print("{}:".format(n))
        for i in range(ceil(n / 2))[1:]:
            #print(i+1, i)
            if (n % ((2 * i) + 1) == 0 or (n - i - 1) % ((2 * i) + 1) == 0):
                print(" {},{}".format(i + 1, i))
            #print(i+1, i+1)
            if (n % (2 * (i + 1)) == 0 or (n - i - 1) % (2 * (i + 1)) == 0):
                print(" {},{}".format(i + 1, i + 1))
    except EOFError:
        break