import sys

level = 0
xml = "".join(sys.stdin)
tags = []
opentags = []
xml = xml.split(">")
for i in range(len(xml) - 1):
    xml[i] = xml[i] + ">"
    tags.append("<" + xml[i].split("<")[1])

for i in range(len(tags)):
    if (tags[i][1] == "/"):
        level -= 1   
        print("{0}{1}".format(((level) * "..."), tags[i]))
    elif (tags[i][-2] == "/"):
        print("{0}{1}".format(((level) * "..."), tags[i]))
    else:
        print("{0}{1}".format(((level) * "..."), tags[i]))
        level += 1