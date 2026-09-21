# Algorithm Correctness and Proof Techniques

Correctness is normally separated into partial correctness and termination. Together they establish total correctness.

## Loop invariants
A loop invariant remains true at a chosen point in every iteration. Prove initialization, maintenance, and termination. In insertion sort, before iteration i the prefix A[0..i-1] is sorted and contains exactly the original prefix elements.

## Mathematical induction
Use base case, inductive hypothesis, and inductive step. It is especially useful for recursive algorithms such as merge sort.

## Exchange arguments
Common for greedy algorithms. Start with an optimal solution, show that the greedy choice can replace an appropriate first choice without reducing quality, then solve the residual instance. Earliest-finish activity selection is the canonical example.

## Cut and cycle properties
For minimum spanning trees, the cut property justifies safe light crossing edges; cycle arguments justify excluding suitable heavy edges. These underpin Kruskal and Prim proofs.

## Contradiction
Assume failure and derive a contradiction with a known invariant, graph property, or mathematical fact.

## Potential-function proofs
For amortized analysis, define nonnegative potential Phi and use amortized cost = actual cost + Phi(after) - Phi(before).

## DP correctness
Prove that every feasible solution is represented, every required transition is considered, optimal substructure makes the recurrence valid, base cases are correct, and dependencies are evaluated first.

## Backtracking correctness
Show every feasible solution appears on some root-to-leaf path and pruning removes only branches that cannot contain a valid solution.

## Proof checklist
Invariant or lemma -> safety of the operation -> termination -> conclusion from the invariant. Avoid phrases such as 'obviously correct' without the supporting property.
