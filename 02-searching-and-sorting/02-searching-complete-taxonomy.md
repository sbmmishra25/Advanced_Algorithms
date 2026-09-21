# Searching Algorithms — Comprehensive Taxonomy

## 1. Sequential
- Linear Search
- Sentinel Linear Search
- Self-Organizing List Search: move-to-front, transpose, frequency count

## 2. Binary and ordered searching
- Binary Search
- Lower Bound
- Upper Bound
- Exponential Search
- Fibonacci Search
- Interpolation Search
- Jump Search
- Ternary Search
- Galloping/Exponential Search
- Binary Search on Answer

## 3. Selection/search in arrays
- Quickselect
- Median of Medians
- Tournament Selection
- Heap-based Top-K

## 4. Hash-based
- Direct addressing
- Hash table lookup
- Cuckoo hashing lookup
- Robin Hood hashing lookup
- Perfect hashing

## 5. Tree-based
- BST search
- AVL search
- Red-Black tree search
- B-tree/B+ tree search
- Trie lookup
- Ternary Search Tree

## 6. String searching
- Naive pattern search
- KMP
- Z algorithm
- Rabin-Karp
- Boyer-Moore
- Horspool
- Sunday algorithm
- Aho-Corasick
- Suffix-array search
- Suffix-tree search
- Suffix automaton based methods

## 7. Graph/state-space search
- BFS
- DFS
- Bidirectional BFS
- Uniform-Cost Search
- Iterative Deepening DFS
- Iterative Deepening A*
- A*
- Best-first search
- Beam search

## 8. Spatial/search structures
- k-d tree
- range tree
- R-tree
- ball tree
- vantage-point tree

## Choosing a method

Sorted static array -> binary/exponential/interpolation depending on distribution.

Unknown/infinite ordered range -> exponential search.

Dictionary membership -> hash table.

Prefix queries -> trie.

Pattern matching -> KMP/Boyer-Moore/Rabin-Karp depending on workload.

Pathfinding -> BFS/Dijkstra/A* depending on edge costs and heuristic information.

Nearest neighbor -> k-d tree/ball tree or approximate NN structures for high dimensions.

## Complexity reminder

Binary search: O(log n).
Linear search: O(n).
Hash lookup: expected O(1) under standard assumptions, but worst cases depend on collision behavior.
