#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here

for i in range(int(read())):
	line = read()
	seconds = line.split()[0]
	seconds = int(seconds)
	title = " ".join(line.split()[1:])
	cyclelength = 0
	if (len(title) <= 17):
		cyclelength = (len(title) + 2) // 2
	else:
		cyclelength = len(title) - 8

	cycle = seconds % cyclelength
	if (cycle <= 9):
		if (cycle == 1):
			print(" " * 8, end="")
		elif (cycle == 2):
			print(" " * 7, end="")
		elif (cycle == 3):
			print(" " * 6, end="")
		elif (cycle == 4):
			print(" " * 5, end="")
		elif (cycle == 5):
			print(" " * 4, end="")
		elif (cycle == 6):
			print(" " * 3, end="")
		elif (cycle == 7):
			print(" " * 2, end="")
		elif (cycle == 8):
			print(" " * 1, end="")
		print(title[:(2 * (cycle - 1)) + 1])
	else:
		print(title[cycle - 9:cycle + 8])