def intersects(c, l):
    x, y, run, rise = l
    

n = int(input())
scene = 1
while n != 0:
    circles = []
    for i in range(n):
        x, y, r = [int(x) for x in input().split()]
        circles.append(((x, y), r))
    ray = [int(x) for x in input().split()]

    hits = []

    # do the math here
    while len(hits) < 11:
        # list of hits
        circle_hits = []
        for i in range(len(circles)):
            if intersects(circles[i], ray) and 1 == 1 : # TODO: case for when ray goes opposite direction
                circle_hits.append(i)
        # if the line hits no spheres, pass
        if len(circle_hits) == 0:
            break

        # otherwise find which one it hits first, recompute ray

        for i in circle_hits:


    print("Scene", scene)
    print(" ".join(hits[:10]), end="")
    print(" ...\n" if len(hits) == 11 else "inf\n")
    n =  int(input())
    scene += 1