while (True):
    try:
        s = input()
        lastAlpha = False
        count = 0
        for c in s:
            if (c.isalpha() == True and lastAlpha == False):
                count += 1
            lastAlpha = c.isalpha()
        print(str(count))
    except EOFError:
        break