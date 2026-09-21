# Complexity Cheatsheet

## Searching
| Algorithm | Best | Average/Expected | Worst | Extra space |
|---|---:|---:|---:|---:|
| Linear search | O(1) | O(n) | O(n) | O(1) |
| Binary search | O(1) | O(log n) | O(log n) | O(1) iterative |
| Hash lookup | O(1) expected | O(1) expected | O(n) | implementation-dependent |
| BST search | O(1) | O(log n) if balanced | O(n) | O(h) recursive |

## Sorting
| Algorithm | Best | Average | Worst | Stable | Extra space |
|---|---:|---:|---:|---|---:|
| Bubble | O(n) | O(n^2) | O(n^2) | Yes | O(1) |
| Insertion | O(n) | O(n^2) | O(n^2) | Yes | O(1) |
| Selection | O(n^2) | O(n^2) | O(n^2) | No* | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | Yes | O(n) |
| Quick | O(n log n) | O(n log n) expected | O(n^2) | No | O(log n) expected stack |
| Heap | O(n log n) | O(n log n) | O(n log n) | No | O(1) |
| Counting | O(n+k) | O(n+k) | O(n+k) | Yes** | O(n+k) |
| Radix | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | Yes** | O(n+k) |

*Variants can be stable. **Depends on the internal stable pass.

## Graphs
BFS/DFS: O(V+E). Topological sort: O(V+E). SCC: O(V+E). Kruskal: O(E log E). Prim with a binary heap: typically O(E log V). Dijkstra with a binary heap: O((V+E) log V). Bellman-Ford: O(VE). Floyd-Warshall: O(V^3).

## DP
Analyze states multiplied by transition cost. Examples: 0/1 knapsack O(nW) pseudo-polynomial, LCS O(nm), matrix-chain O(n^3), bitmask assignment O(n^2 2^n).

## Warning
Expected, amortized, randomized, and model-dependent bounds must be labeled explicitly.
