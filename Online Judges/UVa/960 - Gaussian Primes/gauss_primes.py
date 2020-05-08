import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# list of prime numbers (and bitset)
bs = []
primes = []

# fill the list of prime numbers
def prime_sieve(n):
    global bs, primes
    bs = [True for i in range(n + 1)]
    primes = []
    bs[0] = False
    bs[1] = False
    p = 2
    while (p * p <= n): 
        if (bs[p] == True):
            for i in range(p * 2, n+1, p): 
                bs[i] = False
        p += 1
    for i in range(len(bs)):
        if bs[i]: primes.append(i)

prime_sieve(5000)

