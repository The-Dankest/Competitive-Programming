import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(int(input())):
    a, b = [int(_) for _ in input().strip().split()]
    print("Valid" if a == b else "Invalid")