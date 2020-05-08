l2n = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
n2l = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}

for i in range(int(input())):
    x1, x2, y1, y2 = input().split()
    x2 = int(x2)
    y2 = int(y2)
    x1 = l2n[x1]
    y1 = l2n[y1]
    if (x1 == y1 and x2 == y2):
        print("0 {} {}".format(n2l[x1], x2))
    elif (abs(x1 - y1) == abs(x2 - y2)):
        print("1 {} {} {} {}".format(n2l[x1], x2, n2l[y1], y2))
    elif ((abs(x1 - y1) + abs(x2 - y2)) % 2 == 0):
        print("2 {} {} {} {} {} {}".format(n2l[x1], x2, n2l[(x1 + x2) // 2 + (1 if x1 > y1 else 0)], (x2 + y2) // 2 + (1 if x2 < y2 else 0), n2l[y1], y2))
    else:
        print("Impossible")
