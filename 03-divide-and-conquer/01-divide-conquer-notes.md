# Divide and Conquer

Divide-and-conquer solves a problem by dividing it into smaller independent subproblems, solving them recursively, and combining their results.

## Canonical recurrence
T(n)=aT(n/b)+f(n).

## Core algorithms
- Binary search: divide by two, O(log n).
- Merge sort: two halves plus linear merge, O(n log n).
- Quicksort: partition around a pivot; expected O(n log n), worst O(n^2) for ordinary variants.
- Maximum subarray: recursive combine gives O(n log n); linear Kadane's algorithm is preferable when only the maximum sum is required.
- Counting inversions: merge-sort modification, O(n log n).
- Closest pair of points: O(n log n) divide-and-conquer formulation.
- Strassen matrix multiplication: asymptotically faster than classical multiplication under its assumptions.

## Design checklist
1. Is the problem naturally decomposable?
2. Are subproblems independent?
3. Is the combine step efficient?
4. What recurrence results?
5. Does recursion overhead matter in practice?

## Proof pattern
Prove each recursive call solves its subproblem, prove the combine step is correct, and use induction on input size.
