if __name__ == "__main__":
    ang = 0.0
    guess = 4.5
    off = 1
    last_ang = -1.0
    while (ang != guess):
        if ang < guess - off:
            last_ang = ang
            ang += off
        if ang >= guess - off:
            off = off / 10
        if (last_ang == ang):
            ang += off
            print(ang)
            break
        print(ang, guess)
        
    exit()

d, h, x, n1, n2 = [float(z) for z in input().split()]
while not (d == 0 and h == 0 and x == 0 and n1 == 0 and n2 == 0):
    ang = 0.0

    # FIND THE ANG

    print("{:.2}".format(ang))
    d, h, x, n1, n2 = [float(z) for z in input().split()]