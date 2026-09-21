# Graph Algorithms — Core Notes

Graph algorithms cover traversal, connectivity, ordering, spanning structures, paths, flow, matching, and hard graph problems. These families form a standard core of algorithm-design curricula. citeturn0search0turn0search2

## Representation
- Adjacency list: O(V+E) storage for sparse graphs.
- Adjacency matrix: O(V^2) storage and O(1) edge lookup.
- Edge list: useful for sorting edges and Bellman-Ford/Kruskal.

## Traversal
**BFS** explores by distance layers and is the standard unweighted shortest-path method.

**DFS** explores deeply and supports cycle detection, topological ordering, bridges, articulation points, and SCC algorithms.

## Connectivity
- Connected components: BFS/DFS.
- Bipartite test: 2-color with BFS/DFS.
- Cycle detection: parent tracking for undirected graphs; recursion-stack/three-color logic for directed graphs.
- DSU: incremental connectivity and Kruskal.

## Topological sorting
For a DAG, repeatedly remove indegree-zero vertices (Kahn) or use DFS finishing times. If Kahn processes fewer than V vertices, the graph contains a directed cycle.

## Strongly connected components
- Kosaraju: two DFS passes.
- Tarjan: one DFS with low-link values.

## Bridges and articulation points
DFS discovery times and low-link values identify edges/vertices whose removal increases connectivity.

## Minimum spanning trees
Kruskal uses sorted edges plus DSU. Prim grows a tree by the cheapest crossing edge. Both rely on the MST cut property.

## Eulerian structures
An undirected graph has an Euler circuit when all non-isolated vertices are connected and every degree is even. Euler paths and directed versions require corresponding degree conditions.

## Advanced families
- Lowest common ancestor and binary lifting.
- Heavy-light decomposition.
- Centroid decomposition.
- Euler-tour tree techniques.
- Dynamic connectivity.
- Graph coloring, clique, independent set, Hamiltonian path/cycle.
- Matching and flow.
