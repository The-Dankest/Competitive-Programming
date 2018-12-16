
t = int(input())
curr_guess = []

def printQ():
    global curr_guess
    print("Q", end="")
    for x in curr_guess:
        print(" {}".format(x), end="")

def printA():
    global curr_guess
    print("A", end="")
    for x in curr_guess:
        print(" {}".format(x), end="")

for j in range(t):
    n = int(input())
    curr_guess = [0 for i in range(n)]

    printQ()
    old_right = int(input())
    for i in range(n):
        curr_guess[i] = 1
        printQ()
        new_right = int(input())
        if (new_right == n):
            break
        if (new_right < old_right):
            curr_guess[i] = 0
        else:
            old_right = new_right

    printA()