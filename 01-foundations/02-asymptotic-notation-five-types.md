# Asymptotic Notation — Five Standard Types

The five commonly taught asymptotic notations are **Big-O, Big-Omega, Big-Theta, little-o and little-omega**. They describe growth as n becomes large. citeturn0search0turn0search27

## 1. Big-O: O(g(n))

**Meaning:** asymptotic upper bound.

f(n)=O(g(n)) if there exist constants c>0 and n0 such that:

0 <= f(n) <= c g(n), for all n>=n0.

### Example
f(n)=3n²+5n+7.

For n>=1, f(n)<=15n², so f(n)=O(n²).

### Algorithm example
Two nested loops over n items normally give O(n²).

## 2. Big-Omega: Ω(g(n))

**Meaning:** asymptotic lower bound.

f(n)=Ω(g(n)) if there exist c>0 and n0 such that:

f(n)>=c g(n), for all n>=n0.

For f(n)=3n²+5n+7, f(n)=Ω(n²).

### Algorithm example
Reading all n input elements requires Ω(n) time.

## 3. Big-Theta: Θ(g(n))

**Meaning:** tight asymptotic bound.

f(n)=Θ(g(n)) exactly when f(n)=O(g(n)) and f(n)=Ω(g(n)).

For 3n²+5n+7, f(n)=Θ(n²).

### Algorithm example
Merge sort is Θ(n log n) in its standard implementation.

## 4. Little-o: o(g(n))

**Meaning:** strict asymptotic upper bound.

f(n)=o(g(n)) when:

lim(n→∞) f(n)/g(n) = 0.

Example:
n = o(n²)
because n/n² = 1/n → 0.

But n² is **not** o(n²).

## 5. Little-omega: ω(g(n))

**Meaning:** strict asymptotic lower bound.

f(n)=ω(g(n)) when:

lim(n→∞) f(n)/g(n) = ∞.

Example:
n² = ω(n).

But n² is not ω(n²).

## Relationship

o(g) ⊂ O(g)
ω(g) ⊂ Ω(g)
Θ(g) = O(g) ∩ Ω(g)

## Growth hierarchy

1 < log n < √n < n < n log n < n² < n³ < 2^n < n!

The hierarchy is about asymptotic growth, not exact runtime. citeturn0search0

## Limit-comparison method

For positive functions, examine L=lim f(n)/g(n):
- L=0 -> f=o(g)
- 0<L<∞ -> f=Θ(g)
- L=∞ -> f=ω(g)

## Common mistakes

- O(n²) does not mean exactly n².
- Ω(n) does not automatically mean the algorithm takes at least n operations on every input unless the bound is stated for the relevant case.
- o and ω are strict; Θ is not.
