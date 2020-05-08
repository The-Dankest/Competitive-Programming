import re, math, decimal, bisect, sys
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
nos = 0
for i in range(10):
    print(i)
    sys.stdout.flush()
    if read() == "no":
        nos += 1
if nos > 3:
    print("normal")
else:
    print("grumpy")
sys.stdout.flush()
