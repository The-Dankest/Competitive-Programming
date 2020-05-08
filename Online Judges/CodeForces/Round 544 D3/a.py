import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
h1, m1 = read().strip().split(":")
h2, m2 = read().strip().split(":")
h1 = int(h1)
h2 = int(h2)
m1 = int(m1)
m2 = int(m2)
total_hours = h2 - h1
total_minutes = total_hours * 60 + m2 - m1
total_minutes //= 2
h3 = h1 + (m1 + total_minutes) // 60
m3 = (m1 + total_minutes) % 60
print("{:02d}:{:02d}".format(h3, m3))