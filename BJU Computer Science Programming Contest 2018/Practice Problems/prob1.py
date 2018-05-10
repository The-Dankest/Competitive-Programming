while (True):
    try:
        x = int(input())
        y = int(input())
        print("The sum of {0} and {1} is {2}".format(x, y, x + y))
    except EOFError:
        break