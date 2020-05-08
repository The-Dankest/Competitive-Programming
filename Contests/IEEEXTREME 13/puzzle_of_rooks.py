import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here

n = iread()
rooks = []
end = []
moves = []
for i in range(n):
    a, b = viread()
    rooks.append((a, b))
for i in range(n):
    a, b = viread()
    end.append((a, b))
rooks.sort()
end.sort()

print("Rooks:")
print(*rooks)
print("End:")
print(*end)

l = 0
r = n - 1
# get right columns
while r >= l:
    left_rook = rooks[l]
    if left_rook[0] == end[l][0]:
        l += 1
    elif left_rook[0] > end[l][0]:
        for i in range(abs(left_rook[0] - end[l][0])):
            moves.append(f"{left_rook[0] - i} {left_rook[1]} L")
        rooks[l] = (end[l][0], left_rook[1])
        l += 1
    right_rook = rooks[r]
    if right_rook[0] == end[r][0]:
        r -= 1
    elif right_rook[0] < end[r][0]:
        for i in range(abs(right_rook[0] - end[r][0])):
            moves.append(f"{right_rook[0] + i} {right_rook[1]} R")
        rooks[r] = (end[r][0], right_rook[1])
        r -= 1

print("Rooks:")
print(*rooks)
print("End:")
print(*end)

rooks.sort(key=lambda a: a[1])
end.sort(key=lambda a: a[1])

print("Rooks:")
print(*rooks)
print("End:")
print(*end)

rows = set()
for r in rooks:
    rows.add(r[1])

# get right rows
for i in range(n):
    rook = rooks[i]
    if rook[1] == end[i][1]:
        pass
    elif rook[1] > end[i][1]:
        
    else:
        

print("Rooks:")
print(*rooks)
print("End:")
print(*end)

print(len(moves))
[print(move) for move in moves]