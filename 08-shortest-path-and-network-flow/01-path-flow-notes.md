# Shortest Paths and Network Flow

There is no single shortest-path algorithm that fits every graph model; the choice depends on edge weights, graph density, whether the query is single-source or all-pairs, and whether exact or approximate results are required. citeturn0academia6

## Shortest paths

| Situation | Algorithm |
|---|---|
| Unweighted | BFS |
| DAG | topological-order relaxation |
| Nonnegative weights | Dijkstra |
| Negative edges, no negative cycle | Bellman-Ford |
| All pairs, dense/small V | Floyd-Warshall |
| Sparse all-pairs with possible negative edges | Johnson |
| Single-pair with useful heuristic | A* |

Dijkstra requires nonnegative edge weights. Bellman-Ford also detects reachable negative cycles. Johnson combines reweighting with repeated Dijkstra and handles negative edges when no negative cycle exists. citeturn0search5turn0search12

## Relaxation
For edge (u,v,w), if d[u]+w < d[v], update d[v] and parent[v]. Relaxation is the central operation behind many shortest-path algorithms.

## Network flow
A flow network has capacities on directed edges, a source s and sink t. Residual capacity represents how much additional flow can be sent or undone.

### Ford-Fulkerson
Repeatedly find an augmenting s-t path and send the bottleneck amount. With integer capacities it terminates, but runtime depends on path choices.

### Edmonds-Karp
Use BFS to choose a shortest augmenting path in the residual graph. Its standard bound is O(VE^2). citeturn0search14

### Dinic
Build a level graph with BFS, then send blocking flows with DFS. It is a major practical max-flow implementation.

## Applications
Bipartite matching, scheduling, assignment, transportation, image segmentation, network design, and resource allocation can often be formulated using flow or matching.
