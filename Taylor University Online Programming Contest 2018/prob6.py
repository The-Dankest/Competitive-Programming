#!/usr/bin/env python3
i=0
def read():
	return input().strip()

def f(x : tuple) -> tuple:
	global i
	global fib
	# print(x[0])
	# return (x[0] + 1, fib[x[0]] % i)
	return fib[x] % i

# code goes here
fib = [0, 1]
for j in range(2, 10000):
	fib.append(fib[j - 1] + fib[j - 2])

for j in range(int(read())):
	i = int(read())
	seq = []
	for j in range(1, 10000):
		# seq.append(f(j))
		# print(seq)
		# e = 4 if i // 10000 else (3 if i // 1000 else (2 if i // 100 else (1 if i // 10 else 0)))
		if f(j) == 0:
			
