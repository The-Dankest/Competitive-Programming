import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n = iread()
truth = [x for x in read().split()]
inp = [x for x in read().split()]
stack = []
while len(inp):
    op = inp.pop(0)
    if op == "*":
        a, b, = stack.pop(), stack.pop()
        stack.append(a and b)
    elif op == "+":
        a, b, = stack.pop(), stack.pop()
        stack.append(a or b)
    elif op == "-":
        stack.append(not stack.pop())
    else:
        stack.append(truth[ord(op) - ord("A")] == "T")
print("T" if stack.pop() else "F")
