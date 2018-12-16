import re
while True:
    try:
        line = input()
        values = re.findall("0[xX][0-9a-fA-F]+", line)
        for h in values:
            print("{} {}".format(h, int(h, 0)))
    except EOFError:
        exit()