l = 1
print("1")
print("1 1")
lastline = [1,1]
running = True
_max = pow(10, 60)
while(running):
    line = [1]
    print("1", end="")
    for i in range(l):
        x = lastline[i] + lastline[i + 1]
        print(" {0}".format(x), end="")
        if (x >= _max):
            running = False
        line.append(x)
    l += 1
    line.append(1)
    lastline= line
    print(" 1")