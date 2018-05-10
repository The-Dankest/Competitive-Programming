words = {}
(num, name) = input().strip().split(" ")
while (num != "0"):
    words[int(num)] = name
    (num, name) = input().strip().split(" ")

n = int(input().strip())
while (n != 0):
    printed = False
    for key in sorted(words.keys()):
        if (n % key == 0):
            print(words[key], end="")
            printed = True
    if (not printed):
        print(n, end="")
    print("")
    n = int(input().strip())