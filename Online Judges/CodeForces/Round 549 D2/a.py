import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [_ for _ in input().strip().split()]

# code goes here
n = iread()
doors = "".join(viread()[::-1])
print(min(n - doors.find('1'), n - doors.find('0')))
