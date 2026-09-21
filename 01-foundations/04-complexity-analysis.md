# Complexity Analysis

Complexity analysis studies how resource usage grows with input size. The main resources are time and space.

## Input size
Define n precisely. Arrays use n elements; graphs usually use V and E; integer algorithms may depend on the number of bits.

## Best, worst, average, amortized
- Best case: minimum cost over inputs of size n.
- Worst case: maximum cost.
- Average case: expected cost under a stated probability model.
- Amortized cost: average cost over a sequence, without assuming probabilities.

Example: linear search has best-case Theta(1), worst-case Theta(n), and average Theta(n) under a uniform target-position model.

## Growth-rate reference
| Class | Typical example |
|---|---|
| Theta(1) | array access |
| Theta(log n) | binary search |
| Theta(n) | linear scan |
| Theta(n log n) | merge sort |
| Theta(n^2) | insertion sort worst case |
| Theta(n^3) | Floyd-Warshall |
| Theta(2^n) | subset enumeration |
| Theta(n!) | permutation enumeration |

## Counting loops
A loop that doubles its index runs Theta(log n) times. Independent nested loops multiply their bounds; dependent bounds must be summed. For example, sum(i=1..n) i = Theta(n^2).

## Space complexity
Separate input space, auxiliary space, recursion stack, and output space. Merge sort uses Theta(n) auxiliary array space. In-place quicksort has expected O(log n) stack depth with balanced partitions, but can reach O(n) in the worst case.

## Amortized analysis
Three standard techniques are aggregate, accounting, and potential-function methods. Dynamic-array append is the classic example: occasional Theta(n) resizing still gives O(1) amortized append cost.

## Lower bounds
A lower bound describes a resource requirement that no algorithm in a specified model can beat. Comparison sorting has an Omega(n log n) worst-case lower bound via the decision-tree model; non-comparison sorting can exploit key assumptions.

## Reporting standard
Always state the input model, relevant parameters, case type, space convention, and assumptions.

## Practice
1. Analyze nested loops with dependent bounds.
2. Derive binary-search complexity.
3. Compare recursive and iterative Fibonacci.
4. Prove dynamic-array append is amortized O(1).
5. Derive the comparison-sorting decision-tree lower bound.
