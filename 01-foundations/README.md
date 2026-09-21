# 01 — Foundations

Topics: algorithms and computational thinking, correctness and invariants, Big-O/Theta/Omega, best/average/worst case, recurrence relations, Master theorem, amortized analysis, iterative versus recursive algorithms.

## Example: Linear Search
Scan the array until the target is found.
Time: O(n) worst case. Space: O(1).

Python:
def linear_search(a, target):
    for i, value in enumerate(a):
        if value == target:
            return i
    return -1

Practice:
1. Prove linear search using a loop invariant.
2. Compare linear and binary search.
3. Analyze expected comparisons under a uniform target distribution.