print("{0", end="")
for i in range(1, 10001, 1):
    cycles = 0
    n = i
    while n != 1:
        cycles += 1
        if (n % 2):
            n = (3 * n) + 1
        else:
            n = n / 2
    print(",{0}".format(str(cycles)), end="")
print("};")