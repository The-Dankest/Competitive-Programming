#!/usr/bin/env python3

def read():
	return input().strip()

# code goes here
def cubes(cube):
	a = cube[0]
	b = cube[1]
	c = cube[2]
	d = cube[3]
	e = cube[4]
	f = cube[5]
	return [a + b + c + d + f + e,
	a + c + d + f + e + b,
	a + d + f + b + e + c,
	a + f + b + c + e + d,
	b + a + c + e + d + f,
	b + c + e + f + d + a,
	b + e + f + a + d + c,
	b + f + a + c + d + e,
	c + a + b + e + f + d,
	c + b + e + d + f + a,
	c + e + d + a + f + b,
	c + d + a + b + f + e,
	d + a + f + e + b + c,
	d + f + e + c + b + a,
	d + e + c + a + b + f,
	d + c + a + f + b + e,
	e + b + f + d + a + c,
	e + f + d + c + a + b,
	e + d + c + b + a + f,
	e + c + b + f + a + d,
	f + a + d + e + c + b,
	f + d + e + b + c + a,
	f + e + b + a + c + d,
	f + b + a + d + c + e]

for i in range(int(read())):
	cube = read()
	stop = False
	for a in cubes(cube[:6]):
		for b in cubes(cube[6:12]):
			for c in cubes(cube[12:18]):
				for d in cubes(cube[18:]):
					colors = ["B","G","R","W"]
					face1 = sorted("".join([a[0], b[0], c[0], d[0]]))
					face2 = sorted("".join([a[1], b[1], c[1], d[1]]))
					face3 = sorted("".join([a[3], b[3], c[3], d[3]]))
					face4 = sorted("".join([a[4], b[4], c[4], d[4]]))
					#print(face1)
					#print(face2)
					#print(face3)
					#print(face4)
					if (face1 == colors and face2 == colors and face3 == colors and face4 == colors):
						stop = True
						break
				if (stop):
					break
			if (stop):
				break
		if (stop):
			break

	if (stop):
		print("Yes")
	else:
		print("No")


