# Dynamic Programming — Complete Method

Dynamic programming represents overlapping subproblems as states and reuses their answers. The usual structural signals are optimal substructure and overlapping subproblems.

## DP design recipe
1. Define a state that contains exactly the information needed for the remaining decisions.
2. Write a transition by enumerating the final decision.
3. Specify base cases.
4. Choose an evaluation order that respects dependencies.
5. Store parent or choice information when reconstruction is required.

## Major families
1D: Fibonacci, climbing stairs, house robber, maximum subarray, decode ways.
Knapsack: 0/1, unbounded, bounded, subset sum, partition, target sum.
Sequence: LIS, LCS, edit distance, shortest common supersequence.
Grid: unique paths, minimum path sum, obstacles, grid games.
Interval: matrix-chain multiplication, burst balloons, optimal BST, palindrome partitioning.
Tree: independent set, diameter variants, rerooting.
DAG: longest path, path counting, shortest paths.
Bitmask: TSP, assignment, subset optimization.
Digit DP: counting integers satisfying digit constraints over a range.

## 0/1 knapsack
State dp[i][w] = maximum value using the first i items and capacity w. Transition is max(skip, take) when the item fits. Time O(nW); memory O(W) with rolling arrays. This is pseudo-polynomial because W is a numeric capacity.

## LCS
For strings A and B, if A[i-1] = B[j-1], dp[i][j] = dp[i-1][j-1] + 1; otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Time O(nm). Full O(nm) memory supports reconstruction; two rows support length only.

## Optimization toolbox
Rolling arrays, prefix sums, monotone queues, bitsets, divide-and-conquer optimization, Knuth optimization, convex hull trick, Li Chao tree, state compression, and sparse-state representations. Each requires specific mathematical conditions.

## Greedy versus DP
For every DP problem, test whether a local choice can be exchanged into an optimal solution. If not, seek a counterexample. This turns the greedy-vs-DP distinction into a proof exercise.

## Correctness template
Every valid solution maps to states; every legal final decision is represented; optimal substructure validates the recurrence; base cases are correct; induction over state size proves optimality.

## Practice ladder
Fibonacci; climbing stairs; house robber; 0/1 knapsack; coin change; LIS; LCS; edit distance; matrix-chain multiplication; interval DP; tree DP; digit DP; bitmask TSP; advanced optimized DP.
