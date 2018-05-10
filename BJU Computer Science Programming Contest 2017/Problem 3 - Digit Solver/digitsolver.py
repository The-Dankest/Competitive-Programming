a = input().strip()
b = input().strip()
c = input().strip()

for A in range(0, 10):
    for B in range(0, 10):
        for C in range(0, 10):
            if (int(a.replace("A",str(A)).replace("B",str(B)).replace("C",str(C))) + int(b.replace("A",str(A)).replace("B",str(B)).replace("C",str(C))) == int(c.replace("A",str(A)).replace("B",str(B)).replace("C",str(C)))):
                print(a.replace("A",str(A)).replace("B",str(B)).replace("C",str(C)))
                print(b.replace("A",str(A)).replace("B",str(B)).replace("C",str(C)))
                print(c.replace("A",str(A)).replace("B",str(B)).replace("C",str(C)))
                exit()