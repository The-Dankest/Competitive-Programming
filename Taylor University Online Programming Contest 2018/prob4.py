#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here
m, n = [int(x) for x in read().split()]
list1 = [-1 for i in range(n)]
list2 = [-1 for i in range(n)]
lastDp = list1
dp = list2
lastisone = True
best = 0
for i in range(m):
	line = read()
	# print("i = {}".format(i))
	if i == 0:
		lastDp = [int(c) for c in line]
		# print(*lastDp)
	else:
		# print(lastDp)
		for j in range(n):
			if line[j] == '0':
				dp[j] = 0
			else:
				if j == 0:
					dp[j] = 1
				else:
					corner = lastDp[j - 1]
					top = lastDp[j]
					left = dp[j - 1]
					# print("j = {}".format(j))
					# print("Looking at {},{}: corner = {}, top = {}, left = {}".format(i, j, corner, top, left))
					if 0 in [top, corner, left]:
						dp[j] = 1
					elif top >= corner and left >= corner:
						dp[j] = min(corner, top, left) + 1
					else:
						dp[j] = min(corner, top, left) + 1
					best = max(best, dp[j])
		# print(*dp)
		if lastisone:
			lastisone = False
			dp = list1
			lastDp = list2
		else:
			lastisone = True
			dp = list2
			lastDp = list1
	# print("-------------------------")
print(best)
