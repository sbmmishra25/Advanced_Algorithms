# Algorithm Selection Guide

Start from the problem structure rather than the algorithm name.

| Problem signal | First families to inspect |
|---|---|
| Unsorted membership | linear search, hashing |
| Sorted membership | binary search, interpolation/jump when assumptions fit |
| Need k-th smallest | quickselect, median-of-medians, heap for streaming/top-k |
| Many range-sum queries | prefix sums, Fenwick tree, segment tree |
| Intervals | sorting + greedy, sweep line, interval DP |
| Connectivity | DFS/BFS, DSU |
| Shortest path, unweighted | BFS |
| Shortest path, nonnegative weights | Dijkstra |
| Negative edges | Bellman-Ford; DAG shortest path when graph is a DAG |
| All-pairs shortest paths | Floyd-Warshall, repeated single-source methods, Johnson |
| Minimum spanning tree | Kruskal or Prim |
| Dependencies | topological sort |
| Prefix/string dictionary | trie |
| Exact pattern matching | KMP, Z, Rabin-Karp, Boyer-Moore family |
| Many patterns | Aho-Corasick |
| Optimization with overlapping states | dynamic programming |
| Local-choice proof exists | greedy |
| Need enumerate feasible configurations | backtracking |
| Need optimization with strong bounds | branch and bound |
| Huge search space with meet structure | meet-in-the-middle |
| Integer digit constraints | digit DP |
| Subset-sized n around 20-25 | bitmask DP / meet-in-the-middle |
| Geometric points | orientation, hull, sweep line, spatial trees |
| Approximate NP-hard objective | approximation/local search |
| Adversarial or uncertain input | randomized algorithms may help |

## Questions before choosing
1. What are the constraints?
2. Is the data sorted or sortable cheaply?
3. Is the objective decision, search, counting, or optimization?
4. Are edge weights negative?
5. Is exactness required?
6. Can the state be compressed?
7. Is there a monotonic feasibility predicate enabling binary search on the answer?
8. What assumptions justify the claimed complexity?

The correct choice is determined by constraints and proof conditions, not by popularity.
