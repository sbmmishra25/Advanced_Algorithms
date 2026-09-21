from math import gcd

def fast_power(a, n, mod):
    result = 1
    a %= mod
    while n:
        if n & 1:
            result = result * a % mod
        a = a * a % mod
        n >>= 1
    return result

def sieve(n):
    prime = [True] * (n + 1)
    if n >= 0: prime[0] = False
    if n >= 1: prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            prime[p*p:n+1:p] = [False] * (((n-p*p)//p) + 1)
    return [i for i, ok in enumerate(prime) if ok]

if __name__ == "__main__":
    print(gcd(84, 30))
    print(fast_power(2, 20, 1_000_000_007))
    print(sieve(30))