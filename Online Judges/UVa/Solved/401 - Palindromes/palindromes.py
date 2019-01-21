revs = {"A":"A",
        "B":" ",
        "C":" ",
        "D":" ",
        "E":"3",
        "F":" ",
        "G":" ",
        "H":"H",
        "I":"I",
        "J":"L",
        "K":" ",
        "L":"J",
        "M":"M",
        "N":" ",
        "O":"O",
        "P":" ",
        "Q":" ",
        "R":" ",
        "S":"2",
        "T":"T",
        "U":"U",
        "V":"V",
        "W":"W",
        "X":"X",
        "Y":"Y",
        "Z":"5",
        "1":"1",
        "2":"S",
        "3":"E",
        "4":" ",
        "5":"Z",
        "6":" ",
        "7":" ",
        "8":"8",
        "9":" "}

while (True):
    try:
        s = input().strip()
        pal = True
        rev = True
        for i in range(int(len(s) / 2) + 1):
            # for each character check if the opposite one is the same or reversed
            if (pal == True):
                pal = (s[i] == s[len(s) - i - 1])
            if (rev == True):
                rev = (revs[s[i]] == s[len(s) - i - 1])
        if (pal and rev):
            print("{0} -- is a mirrored palindrome.".format(s))
        elif (not pal and rev):
            print("{0} -- is a mirrored string.".format(s))
        elif (pal and not rev):
            print("{0} -- is a regular palindrome.".format(s))
        else:
            print("{0} -- is not a palindrome.".format(s))
        print("")
    except EOFError:
        break