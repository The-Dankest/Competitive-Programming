import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# code goes here
for i in range(iread()):
    k, n = viread()
    fract1_num = k ** n
    fract2_num = 1
    if k >= n:
        for i in range(n):
            fract2_num *= k - i
    else:
        fract2_num = 0

    deno = (k + 1) ** (n + 1)

    # print
    fract1_div = gcd(deno, fract1_num)
    fract2_div = gcd(deno, fract2_num)
    print("{}, {}".format(0 if fract1_num == 0 else "{}/{}".format(fract1_num // fract1_div, deno // fract1_div), 0 if fract2_num == 0 else "{}/{}".format(fract2_num // fract2_div, deno // fract2_div)))
