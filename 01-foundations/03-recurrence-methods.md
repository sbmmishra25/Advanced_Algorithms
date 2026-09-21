# Recurrences: Substitution, Recursion Tree, Master Method and Beyond

## Why recurrences?

Recursive algorithms are naturally described by equations relating T(n) to smaller inputs.

Example:
T(n)=2T(n/2)+n.

## 1. Substitution method

### Procedure
1. Guess a bound.
2. Substitute the inductive hypothesis.
3. Choose constants so the inequality closes.
4. Verify the base case.

### Example
T(n)=2T(n/2)+n.

Guess T(n)=O(n log n).
Assume T(n/2)<=c(n/2)log(n/2).

Then:
T(n)<=cn log(n/2)+n
=cn log n - cn + n.
For sufficiently large c, this is <=cn log n.

Therefore T(n)=O(n log n).

The matching lower bound gives Θ(n log n).

## 2. Recursion-tree method

Expand the recurrence level by level.

For T(n)=2T(n/2)+n:
- Level 0 cost: n
- Level 1 cost: n
- ...
- Number of levels: log2 n
- Total: Θ(n log n)

## 3. Master method

For T(n)=aT(n/b)+f(n), compare f(n) with n^(log_b a). Standard cases give Θ(n^(log_b a)), Θ(n^(log_b a)log n), or Θ(f(n)) under the required regularity condition. citeturn0search1turn0search27

### Case 1
f(n)=O(n^(log_b a-epsilon)).
Then T(n)=Θ(n^(log_b a)).

Example:
T(n)=4T(n/2)+n -> Θ(n²).

### Case 2
f(n)=Θ(n^(log_b a) log^k n).
Then T(n)=Θ(n^(log_b a) log^(k+1)n).

Example:
T(n)=2T(n/2)+n -> Θ(n log n).

### Case 3
f(n)=Ω(n^(log_b a+epsilon)) plus regularity.
Then T(n)=Θ(f(n)).

Example:
T(n)=2T(n/2)+n² -> Θ(n²).

## 4. When Master theorem does not directly apply

Examples:
- unequal subproblem sizes
- non-polynomially related subproblems
- irregular recursion
- recurrences with floor/ceiling effects requiring care

## 5. Akra–Bazzi

For advanced analysis, use Akra–Bazzi for forms such as:
T(x)=Σ a_i T(b_i x+h_i(x))+g(x).

## Practice

Solve:
1. T(n)=T(n/2)+1
2. T(n)=2T(n/2)+n
3. T(n)=2T(n/2)+n log n
4. T(n)=3T(n/2)+n
5. T(n)=T(n-1)+n
6. T(n)=T(n/3)+T(2n/3)+n
7. T(n)=2T(n/2)+n²
