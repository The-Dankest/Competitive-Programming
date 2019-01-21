a, b = input().strip().split()
while (not (a == "0" and b == "0")):
    if (len(a) > len(b)):
        b = ((len(a) - len(b)) * "0") + b
    elif (len(b) > len(a)):
        a = ((len(b) - len(a)) * "0") + a
    c = 0
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + c
        if (s > 9):
            carry += 1
            c = 1
        else:
            c = 0
    if (carry == 0):
        print("No carry operation.")
    elif (carry == 1):
        print("1 carry operation.")
    else:
        print("{0} carry operations.".format(carry))
    a, b, = input().strip().split()