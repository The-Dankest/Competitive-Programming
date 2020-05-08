# BJU Bitwise Blitz 
# prob8.py

import math, re, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
line = read()
i = 1
ttl = 0
while not line.startswith("THE END"):
    code = "" if line != "" else '0'
    for thing in line.split():
        code += str(len(thing))
    print("Line {} = {}".format(i, code))
    i += 1
    ttl += int(code)
    line = read()
print("Sum of file = {}".format(ttl))
