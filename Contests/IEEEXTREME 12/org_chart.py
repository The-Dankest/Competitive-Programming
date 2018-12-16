class div:
    parent = ""
    low = 0
    up = 0
    def __init__(self, p, l, u):
        parent = p
        low = l
        up = u

n, q = [int(x) for x in input().split()]
divs = {}
for i in range(n):
    _in = input().split()
    divs[_in[0]] = div(_in[1], int(_in[2]), int(_in[3]))
for i in range(q):
    _div, t = input().split()
    
    if (divs[_div].low != 0 and divs[_div].up != 0):
        print()
    elif (t == "1"):
