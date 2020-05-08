import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    n = iread()
    r1, p1, s1 = viread()
    hands = read()
    r2, p2, s2 = hands.count("R"), hands.count("P"), hands.count("S")
    if (min(r2, p1) + min(p2, s1) + min(s2, r1) >= math.ceil(n / 2)):
        print("YES")
        burn = ("r" * (r1 - min(s2, r1))) + ("p" * (p1 - min(r2, p1))) + ("s" * (s1 - min(p2, s1)))
        burn = list(burn)
        ans = hands.replace("R", "p", min(r2, p1)).replace("P", "s", min(p2, s1)).replace("S", "r", min(s2, r1))
        for c in ans:
            if c < "a":
                print(burn.pop().upper(), end="")
            else:
                print(c.upper(), end="")
        print()
    else:
        print("NO")