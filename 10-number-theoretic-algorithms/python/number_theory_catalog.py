"""Core number-theoretic algorithms."""

from math import gcd

def extended_gcd(a,b):
    if b==0:return (abs(a),1 if a>=0 else -1,0)
    g,x1,y1=extended_gcd(b,a%b)
    return g,y1,x1-(a//b)*y1

def mod_pow(a,e,m):
    if m<=0:raise ValueError("modulus must be positive")
    result=1%m;a%=m
    while e:
        if e&1:result=result*a%m
        a=a*a%m;e>>=1
    return result

def mod_inverse(a,m):
    g,x,_=extended_gcd(a,m)
    if g!=1:raise ValueError("inverse does not exist")
    return x%m

def sieve(n):
    if n<2:return []
    prime=[True]*(n+1);prime[0]=prime[1]=False
    p=2
    while p*p<=n:
        if prime[p]:prime[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
        p+=1
    return [i for i,v in enumerate(prime) if v]

def segmented_sieve(left,right):
    if right<left:return []
    limit=int(right**0.5)
    primes=sieve(limit);is_prime=[True]*(right-left+1)
    for p in primes:
        start=max(p*p,((left+p-1)//p)*p)
        for x in range(start,right+1):is_prime[x-left]=False
    for x in range(left,min(right+1,2)):is_prime[x-left]=False
    return [left+i for i,v in enumerate(is_prime) if v]
