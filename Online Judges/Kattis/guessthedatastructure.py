while True:
    try:
        stack = True
        queue = True
        pqueue = True
        for i in range(int(input())):
            x, y = [int(z) for z in input().split()]
            s = []
            q = []
            p = []
            if (x == 1):
                s.append(y)
                q = [y] + q
                p.append(y)
                p = sorted(p)
            else:
                if (len(s) > 0):
                    if (s.pop() != y):
                        stack = False
                else:
                    stack = False
                if (len(q) > 0):
                    if (q.pop() != y):
                        queue = False
                else:
                    queue = False
                if (len(p) > 0):
                    if (p.pop() != y):
                        pqueue = False
                else:
                    pqueue = False
        print(stack, queue, pqueue)
        if ((stack and queue) or (queue and pqueue) or (stack and pqueue)):
            print("not sure")
        elif (stack):
            print("stack")
        elif (queue):
            print("queue")
        elif (pqueue):
            print("priority queue")
        else:
            print("impossible")
    except EOFError:
        break