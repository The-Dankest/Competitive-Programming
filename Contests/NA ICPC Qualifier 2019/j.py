import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n = iread()
nums = viread()

left_avg = [[nums[0], 1]]
right_avg = [[nums[-1], 1]]
ans = max(max(nums[-1], 0), nums[0])
for i in range(n - 1):
    d = left_avg[i][1]
    left_avg.append([((left_avg[i][0] * d) + nums[i + 1]) / (d + 1), d + 1])
    right_avg.append([((right_avg[i][0] * d) + nums[-2 - i]) / (d + 1), d + 1])
    ans = max(max(left_avg[i + 1][0], right_avg[i + 1][0]), ans)

print(f"{ans:.9f}")
    
