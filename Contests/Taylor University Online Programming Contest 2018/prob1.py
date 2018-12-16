#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here
for i in range(int(read())):
	b, e, s = read().split()
	b = float(b)
	e = float(e)
	s = float(s)
	l = []
	print("[", end="")
	if (b < e and s > 0):
		l.append(b)
		next_l = b + s
		i = 2
		while(next_l < e):
			l.append(round(next_l, 4))
			next_l = b + (s * i)
			i += 1
		print("{:0.4f}".format(l[0]), end="")
		for i in range(1, len(l)):
			print(", {:0.4f}".format(l[i]), end="")
	elif (b > e and s < 0):
		l.append(b)
		next_l = b + s
		i = 2
		while(next_l > e):
			l.append(round(next_l, 4))
			next_l = b + (s * i)
			i += 1
		print("{:0.4f}".format(l[0]), end="")
		for i in range(1, len(l)):
			print(", {:0.4f}".format(l[i]), end="")
	print("]")