# list of prime numbers (and bitset)
bs = []
primes = []

# check if a number is prime
def is_prime(n):
    if n in primes:
        return True
    for p in primes:
        if (n % p == 0):
            return False
    return True

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

# get prime factors of a number
def prime_factors(n): 
    factors = []
    pf = 0
    while primes[pf] ** 2 < n:
        while n % primes[pf] == 0:
            factors.append(primes[pf])
            n //= primes[pf]
        pf += 1
    if n != 1:
        factors.append(n)
    return factors