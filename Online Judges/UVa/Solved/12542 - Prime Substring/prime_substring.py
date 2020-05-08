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

prime_sieve(100000)

# code goes here
n = read()
while (n != "0"):
    largest = 0
    for length in range(5)[::-1]:
        for i in range(len(n) - length):
            num = int(n[i:i + length + 1])
            prime_pos = bisect.bisect(primes, num) - 1
            if primes[prime_pos] == num:
                largest = max(num, largest)
        if (largest != 0 and len(str(largest)) > length):
            break
    print(largest)
    n = read()
