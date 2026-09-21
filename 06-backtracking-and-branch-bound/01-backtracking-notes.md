# Backtracking and Branch & Bound

## Backtracking
Backtracking systematically explores a state space and abandons a partial state as soon as it cannot lead to a valid solution.

Core examples:
- N-Queens.
- Sudoku.
- graph coloring.
- Hamiltonian cycle.
- subset sum.
- permutations/combinations.
- cryptarithmetic.
- exact cover.

## Pruning
Useful pruning rules include constraint violation, remaining-capacity checks, symmetry breaking, variable ordering, value ordering, and constraint propagation.

## Branch and bound
Branch-and-bound targets optimization. Each node represents a partial solution and receives a bound on the best achievable completion. If the bound cannot beat the incumbent solution, prune the node.

Common examples:
- 0/1 knapsack.
- TSP.
- assignment.
- scheduling.
- integer programming.

## Correctness
Backtracking is complete if every feasible solution has a represented path and pruning removes only impossible states. Branch-and-bound additionally requires a valid optimistic bound.

## Complexity
Worst-case behavior is often exponential or factorial. The practical value comes from strong pruning and good ordering; report both worst-case complexity and assumptions.
