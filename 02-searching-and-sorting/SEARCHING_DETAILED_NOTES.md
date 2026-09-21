# Searching Algorithms — Detailed Notes, Examples, Complexity and Use Cases

## 1. Linear Search
Inspect elements from left to right until the target is found.

Example: search 7 in [4,9,2,7,5] -> inspect 4,9,2 -> find 7 at index 3.

Time: Best O(1), Average O(n), Worst O(n). Space O(1).

Use: unsorted data, linked lists, small datasets.

## 2. Sentinel Linear Search
Place the target temporarily at the end so the loop can avoid a boundary check in every iteration.

Time O(n) worst case. Space O(1) with a spare position. It is an implementation optimization, not a different asymptotic class.

## 3. Binary Search
Requires sorted data and repeatedly halves the search interval.

Example: search 23 in [3,8,12,17,23,31,42]:
middle 17 -> right half; middle 31 -> left half; find 23.

Time: Best O(1), Average/Worst O(log n). Space O(1) iterative or O(log n) recursive.

## 4. Lower Bound and Upper Bound
For sorted data:
- lower_bound(x): first index with value >= x.
- upper_bound(x): first index with value > x.

Example [1,2,2,2,5]: lower_bound(2)=1 and upper_bound(2)=4.

Time O(log n).

## 5. Jump Search
Jump through blocks of about sqrt(n), then linearly search the identified block.

Time O(sqrt(n)) worst case. Space O(1). Requires sorted data.

## 6. Interpolation Search
Estimates a likely position from the numeric values:

pos = lo + (target-A[lo])*(hi-lo)/(A[hi]-A[lo]).

Expected O(log log n) for suitable uniform distributions; worst O(n). Space O(1).

The O(log log n) statement is distribution-dependent and must not be presented as universal.

## 7. Exponential Search
Probe positions 1,2,4,8,... until a range containing the target is found, then perform binary search.

Time O(log n) on an ordinary sorted array; more precisely O(log p) when p is the target position in an effectively unbounded sorted sequence. Space O(1).

## 8. Fibonacci Search
Uses Fibonacci-number offsets rather than midpoint division.

Time O(log n). Space O(1).

Mainly useful as an educational alternative and for certain access-cost models.

## 9. Ternary Search
For a unimodal function, compare two interior points and discard one region.

Time O(log n) for the standard unimodal-search setting. Space O(1) iterative.

For ordinary sorted-array lookup, binary search is generally more comparison-efficient.

## 10. Galloping Search
Exponentially expands the search range and then binary-searches it. It is useful when a target is likely to occur near the beginning of a sorted range and in merge operations.

## 11. Quickselect
Partition like quicksort but recurse only into the side containing the kth element.

Example: [7,2,1,8,6,3,5,4], k=3 -> fourth-smallest value is 4.

Average/Expected O(n), Worst O(n²) for ordinary pivot choices. Space O(log n) expected recursive stack, with implementation-dependent worst case.

## 12. Median of Medians
Chooses a deterministic pivot with a linear-time worst-case selection guarantee.

Worst-case O(n). Space depends on implementation.

Use when a deterministic worst-case linear selection bound matters.

## 13. Hash-Based Search
Map keys to buckets using a hash function.

Expected O(1) lookup under suitable assumptions; simple implementations can degrade to O(n) worst case. Space O(n).

Use when ordering is unnecessary and fast expected membership is important.

## 14. Binary Search Tree
Follow left/right comparisons according to the key.

Time O(h), where h is tree height. Balanced trees give O(log n); a skewed tree gives O(n). Structure space O(n).

## 15. Balanced BST
AVL and Red-Black trees maintain logarithmic height.

Search, insertion and deletion are O(log n) worst case.

## 16. Trie Search
For a string of length L, lookup is O(L) under the standard character-operation model.

Use for prefix queries, dictionaries and autocomplete.

## 17. Exact String Search
Naive matching is O(nm) worst case. KMP and Z are O(n+m). Rabin-Karp is expected efficient with verification when exact matching is required.

## 18. Binary Search on Answer
Search the smallest or largest value satisfying a monotone feasibility predicate.

Example: minimize the maximum workload assigned to k workers. Define feasible(x) as whether all work can be completed with maximum load x. If feasibility changes once from false to true, binary search applies.

Time O(log R * F), where R is the answer range and F is one feasibility-check cost.

## Master comparison

| Algorithm | Requirement | Best | Average/Expected | Worst | Extra space |
|---|---|---:|---:|---:|---:|
| Linear | none | O(1) | O(n) | O(n) | O(1) |
| Binary | sorted | O(1) | O(log n) | O(log n) | O(1) iterative |
| Jump | sorted | O(1) | O(sqrt n) | O(sqrt n) | O(1) |
| Interpolation | sorted + suitable distribution | O(1) | O(log log n) expected | O(n) | O(1) |
| Exponential | sorted | O(1) | O(log n) | O(log n) | O(1) |
| Fibonacci | sorted | O(1) | O(log n) | O(log n) | O(1) |
| Quickselect | array | O(n) favorable | O(n) expected | O(n²) | implementation-dependent |
| Median of medians | array | O(n) | O(n) | O(n) | implementation-dependent |
| Hash table | hashable keys | O(1) expected | O(1) expected | O(n) | O(n) |
| Balanced BST | ordered keys | O(log n) | O(log n) | O(log n) | O(n) structure |
| Trie | strings | O(L) | O(L) | O(L) | O(total characters) |

## Practice
1. First occurrence of a duplicate.
2. Last occurrence.
3. Count occurrences with two bounds.
4. Search a rotated sorted array.
5. Find a peak element.
6. Integer square root.
7. Minimize maximum pages/workload.
8. kth smallest.
9. Median of two sorted arrays.
10. Search in an implicit sorted sequence.
