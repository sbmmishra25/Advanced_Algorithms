# Greedy Algorithms — Method, Proofs, and Core Problems

A greedy algorithm builds a solution step by step, committing to a locally attractive choice. The choice must be justified; intuition alone is not a proof.

## Workflow
1. Define the objective.
2. Identify the local choice.
3. State the greedy-choice property.
4. Prove the choice is safe.
5. Reduce to the residual problem.
6. Repeat.

## Activity selection
Given intervals (start, finish), maximize compatible activities. Choose the compatible activity with earliest finish time. Exchange proof: if an optimal solution starts with o and greedy chooses g, finish(g) <= finish(o), so replacing o by g cannot reduce the remaining feasible set. Sorting costs O(n log n), scanning O(n).

## Fractional knapsack
Sort by value/weight ratio and take the highest density first. The exchange argument proves that replacing lower-density material by higher-density material never hurts. This proof does not transfer to 0/1 knapsack.

## Job sequencing with deadlines
For unit-time jobs, sort by descending profit and put each job in the latest available slot not exceeding its deadline. This preserves earlier slots for jobs with tighter deadlines.

## Huffman coding
Repeatedly merge the two least frequent symbols. A min-priority queue gives O(n log n) construction. The proof uses the sibling property of an optimal prefix-code tree.

## Minimum spanning trees
Kruskal sorts edges and adds a safe edge joining different components; DSU supports component tests. Prim repeatedly chooses the minimum edge crossing the current tree cut. Both are justified by the MST cut property.

## Dijkstra
For nonnegative edge weights, repeatedly finalize the unsettled vertex with minimum tentative distance. Negative edges invalidate the standard greedy proof.

## Greedy failure examples
Naive greedy can fail for 0/1 knapsack, weighted interval scheduling, and general coin change. Construct a small counterexample to identify the missing property.

## Proof checklist
What is the local choice? Why is it feasible? Can an optimal solution be transformed to include it? Does the residual problem have the same structure? What assumptions are required?

## Practice ladder
Activity selection; fractional knapsack; job sequencing; Huffman; Kruskal; Prim; Dijkstra; minimum platforms; optimal merge; set-cover approximation; metric-TSP approximation.
