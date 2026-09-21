# Sorting Algorithms — Detailed Notes, Examples, Complexity and Use Cases

This file expands the sorting catalogue into actual teaching notes. The complexity tables use standard teaching implementations; variants can change constants, stability, and auxiliary space. citeturn0search0turn0search1

## 1. Bubble Sort
**Idea:** repeatedly compare adjacent elements and swap an out-of-order pair. After each pass, one largest remaining element reaches the end.

Example: [5,1,4,2] -> pass 1 [1,4,2,5] -> pass 2 [1,2,4,5].

Time: Best O(n) with early stopping; Average O(n²); Worst O(n²). Space: O(1). Stable: Yes. In-place: Yes.

Use it mainly for teaching and very small/nearly sorted inputs. citeturn0search7

## 2. Selection Sort
**Idea:** find the minimum in the unsorted suffix and swap it into the next position.

Example: [64,25,12,22,11] -> [11,25,12,22,64] -> [11,12,25,22,64] -> [11,12,22,25,64].

Time: Best/Average/Worst O(n²). Space: O(1). Stable: No in the usual implementation. In-place: Yes.

A useful property is that it performs only O(n) swaps. citeturn0search0turn0search1

## 3. Insertion Sort
**Idea:** maintain a sorted prefix and insert each next element into its correct position.

Example: [5,2,4,6] -> [2,5,4,6] -> [2,4,5,6] -> [2,4,5,6].

Time: Best O(n), Average/Worst O(n²). Space: O(1). Stable: Yes. In-place: Yes. Adaptive: Yes.

Use it for small or nearly sorted arrays and as a component of hybrid algorithms. citeturn0search1turn0search7

## 4. Merge Sort
**Idea:** split into halves, recursively sort, then merge two sorted halves.

Example: [38,27,43,3] -> [27,38] and [3,43] -> [3,27,38,43].

Recurrence: T(n)=2T(n/2)+Theta(n), giving Theta(n log n).

Time: Best/Average/Worst O(n log n). Space: O(n) for the standard array implementation. Stable: Yes. citeturn0search1

Use when stable sorting and guaranteed O(n log n) time are important; it is also fundamental to external sorting.

## 5. Quick Sort
**Idea:** choose a pivot, partition smaller and larger elements, then recursively sort the partitions.

Example: [9,3,7,1,8], pivot 7 -> [3,1] 7 [9,8] -> fully sort both sides.

Time: Best/Average O(n log n); Worst O(n²) with repeatedly unbalanced partitions. Space: O(log n) expected stack for balanced recursion and O(n) worst case for a simple recursive implementation. Stable: No. citeturn0search9

Improvements include randomized pivots, median-of-three, three-way partitioning and introsort.

## 6. Heap Sort
**Idea:** build a max heap, repeatedly move the maximum to the end, and restore the heap.

Example: [4,10,3,5,1] -> build max heap -> extract 10, then 5, then 4, then 3, then 1.

Time: Best/Average/Worst O(n log n). Space: O(1) auxiliary. Stable: No. In-place: Yes.

Use when worst-case O(n log n) time and constant auxiliary array space are priorities.

## 7. Counting Sort
**Idea:** count occurrences of each key rather than compare elements.

Example: [4,2,2,8,3,3,1] -> counts of 1..8 -> [1,2,2,3,3,4,8].

For key range k: Time O(n+k). Space O(k), or O(n+k) for a stable output-array implementation. Stable: Yes when implemented with cumulative positions and a stable output pass.

Use for integer/small bounded keys. It is not a comparison sort. citeturn0search8

## 8. Radix Sort
**Idea:** process digits/characters one position at a time using a stable inner sort.

Example: 170,45,75,90,802,24,2,66 -> sort by ones -> tens -> hundreds -> final sorted order.

For d digits and digit range k: Time O(d(n+k)); Space commonly O(n+k). Stability: Yes if each digit pass is stable.

Use for fixed-width integers, strings and structured keys. citeturn0search0

## 9. Bucket Sort
**Idea:** distribute values into buckets, sort each bucket, then concatenate.

Example: values in [0,1) are placed into intervals such as [0,.1), [.1,.2), etc.

Expected Time O(n+k) under suitable distribution assumptions; common worst case O(n²). Space O(n+k). Stability depends on the bucket sorter.

Use when values are reasonably uniformly distributed over a known range.

## 10. Shell Sort
**Idea:** perform insertion-sort-like passes with decreasing gaps, finishing with gap 1.

Time depends strongly on the gap sequence. Classic simple sequences have O(n²) worst-case behavior. Space O(1). Stable: No. In-place: Yes.

It is useful for studying how preprocessing with distant comparisons can improve insertion sort.

## 11. TimSort
**Idea:** detect naturally ordered runs, use insertion sort on short runs, then merge runs.

Time: Best O(n); Average/Worst O(n log n). Space: O(n) in standard implementations. Stable: Yes. Adaptive: Yes. citeturn0search3

Python sorted() and list.sort() use TimSort-family behavior. citeturn0search2

## 12. IntroSort
**Idea:** begin with quicksort, switch to heapsort when recursion becomes too deep, and use insertion sort for small partitions.

Time: O(n log n) worst case. Space: typically O(log n) stack. Stable: No.

C++ std::sort is commonly implemented with an introspective strategy, although exact library implementations may vary. citeturn0search2

## 13. Cocktail Shaker Sort
Bidirectional bubble sort: sweep left-to-right and then right-to-left.

Time: Best O(n) with early stopping; Average/Worst O(n²). Space O(1). Stable: Yes.

## 14. Comb Sort
Starts with a large gap and repeatedly shrinks it, ending with bubble-like adjacent comparisons.

Typical teaching bound: Worst O(n²), Space O(1). Stable: No.

## 15. Gnome Sort
Walk forward when adjacent values are ordered; otherwise swap and step backward.

Best O(n); Average/Worst O(n²). Space O(1). Stable: Yes.

## 16. Cycle Sort
Moves elements directly to their final positions through cycles.

Time O(n²) comparisons, but only O(n) writes. Space O(1). Stable: No.

Useful when writes are significantly more expensive than comparisons.

## 17. Pancake Sort
Repeatedly find the maximum in the unsorted prefix and move it to the end using prefix reversals.

Time O(n²). Space O(1). Stable: No.

## 18. Bitonic Sort
A sorting-network algorithm that constructs bitonic sequences and applies compare-exchange operations.

Time O(n log² n), parallel depth O(log² n). It is important for parallel hardware and fixed comparison networks.

## 19. Odd-Even Merge / Sorting Networks
A sorting network executes a predetermined sequence of compare-exchange operations independent of the input values.

Use: parallel hardware, SIMD-style environments and deterministic comparison networks.

## 20. External Merge Sort
When data does not fit in RAM:
1. Read a memory-sized chunk.
2. Sort it.
3. Write a sorted run.
4. Merge runs using multiple sequential passes.

The important resource becomes disk/storage I/O, not only RAM operations. citeturn0search5

## Stability
A stable sort preserves the relative order of records with equal keys.

Example records: (AI,2), (DB,1), (ML,2). Stable sorting by the second field gives (DB,1), (AI,2), (ML,2).

## Master comparison

| Algorithm | Best | Average | Worst | Extra space | Stable | In-place |
|---|---:|---:|---:|---:|---|---|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No* | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No* |
| Quick | O(n log n) | O(n log n) expected | O(n²) | O(log n) expected | No | Yes* |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes* | No |
| Radix | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes* | No |
| Bucket | O(n+k) expected | O(n+k) expected | O(n²) | O(n+k) | Depends | Depends |
| TimSort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Shell | gap-dependent | gap-dependent | O(n²) classic | O(1) | No | Yes |
| Bitonic | O(n log² n) | O(n log² n) | O(n log² n) | O(n) | No | No |

*Variant dependent.

## Learning requirement
For every sorting algorithm, students should be able to explain the idea, trace a small example, prove correctness, derive time and space complexity, identify best/worst input, state stability/in-place properties, and explain when the algorithm should or should not be used.
