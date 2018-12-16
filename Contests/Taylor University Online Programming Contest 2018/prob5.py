#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here
for i in range(int(read())):
	print(12*2**(int(read()) - 1))

