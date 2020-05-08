import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
while (True):
    try:
        l, w, h, angle = viread()
        vol = ((l * h * w) - ((l * math.tan(math.pi * 2 / 360 * angle)) * l / 2) * w) 
        print("{:0.3f} mL".format(vol)) 
    except EOFError:
        break
