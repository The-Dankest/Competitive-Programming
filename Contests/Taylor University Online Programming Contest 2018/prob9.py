#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here
n = int(read())
while n != 0:
	s = n / 2
	print("{:.3f}".format( (((n*n - s*s)**(1/2))**2 - s*s)**(1/2) ))

	n= int(read())
