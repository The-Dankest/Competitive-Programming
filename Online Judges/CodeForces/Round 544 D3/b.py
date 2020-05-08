import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here

n, k = viread()
boxes = []
zero_count = 0
for box in viread():
    if box % k == 0:
        zero_count += 1
    else:
        boxes.append(box % k)
boxes.sort()

start = 0
end = len(boxes) - 1
ans = (zero_count // 2) * 2
while (start < end):
    this_count = boxes[start] + boxes[end]
    if this_count < k:
        start += 1
    elif this_count == k:
        ans += 2
        start += 1
        end -= 1
    else:
        end -=1
print(ans)