prog_a = []
prog_b = []
line = input().strip()
while (line != "E"):
    prog_a.append(line.split())
    line = input().strip()
line = input().strip()
while (line != "E"):
    prog_b.append(line.split())
    line = input().strip()

for i in range(len(prog_a)):
    