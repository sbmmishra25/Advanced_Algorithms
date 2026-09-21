# Sorting Algorithms — Comprehensive Taxonomy

There is no finite list of literally every sorting algorithm ever invented; new variants and domain-specific methods continue to appear. This catalog covers the major classical, practical, educational, distribution, hybrid, network and unusual families. University course material itself lists a very broad collection including IntroSort, TimSort, CubeSort, CycleSort, LibrarySort, PatienceSort, SmoothSort, StrandSort, TournamentSort, CocktailSort, CombSort, GnomeSort, BlockSort, Odd-Even Sort, Pigeonhole, SpreadSort, BurstSort, FlashSort, PostmanSort, BeadSort, PancakeSort, SpaghettiSort, BitonicSort, BogoSort and others. citeturn0search30

## A. Comparison-based elementary sorts
1. Bubble Sort
2. Cocktail Shaker Sort
3. Comb Sort
4. Gnome Sort
5. Insertion Sort
6. Selection Sort
7. Cycle Sort
8. Pancake Sort
9. Strand Sort
10. Odd-Even Sort

## B. Efficient comparison sorts
11. Merge Sort
12. Bottom-up Merge Sort
13. Natural Merge Sort
14. Quick Sort
15. Dual-Pivot Quick Sort
16. Three-Way Quick Sort
17. Heap Sort
18. Tournament Sort
19. Tree Sort
20. SmoothSort
21. Shell Sort

## C. Hybrid/practical sorts
22. TimSort
23. IntroSort
24. Block Sort
25. WikiSort
26. GrailSort
27. Library Sort
28. SpreadSort

## D. Non-comparison/distribution sorts
29. Counting Sort
30. Pigeonhole Sort
31. Bucket Sort
32. Radix Sort — LSD
33. Radix Sort — MSD
34. American Flag Sort
35. FlashSort
36. BurstSort
37. Postman Sort

## E. String/specialized sorting
38. MSD string sort
39. LSD string sort
40. BurstSort
41. Trie-based sorting
42. Patience Sorting

## F. Parallel/network sorts
43. Bitonic Sort
44. Odd-Even Merge Sort
45. Sorting Networks
46. Batcher's Bitonic Network
47. Batcher's Odd-Even Merge Network

## G. Educational/impractical sorts
48. Stooge Sort
49. Slow Sort
50. Bogo Sort
51. Bozo Sort
52. Stalin Sort (pedagogical/non-general-purpose)

## Comparison table

| Algorithm | Family | Typical time | Stable? | Main idea |
|---|---|---:|---|---|
| Bubble | exchange | Θ(n²) | Yes | adjacent swaps |
| Insertion | insertion | Θ(n²) | Yes | insert into sorted prefix |
| Selection | selection | Θ(n²) | Usually no | repeatedly select minimum |
| Merge | divide/conquer | Θ(n log n) | Yes | split and merge |
| Quick | partition | avg Θ(n log n) | No | pivot partition |
| Heap | heap | Θ(n log n) | No | heap selection |
| TimSort | hybrid | O(n log n), adaptive | Yes | runs + merge/insertion |
| IntroSort | hybrid | O(n log n) worst | No | quicksort + heap fallback |
| Counting | distribution | Θ(n+k) | Yes with standard stable form | frequency counts |
| Radix | distribution | O(d(n+k)) | Yes with stable pass | digit-by-digit |
| Bucket | distribution | expected near-linear under assumptions | implementation-dependent | distribute into buckets |
| Bitonic | network | O(log² n) depth | N/A | compare-exchange network |

Practical performance depends on data distribution, memory hierarchy, language and implementation; theoretical complexity alone does not determine the fastest method. citeturn0search2turn0search5

## Sorting decision guide

- Nearly sorted -> insertion / TimSort
- General-purpose -> TimSort / IntroSort / tuned QuickSort
- Guaranteed O(n log n), low extra memory -> HeapSort
- Stable general-purpose -> MergeSort / TimSort
- Small integer range -> Counting / Pigeonhole
- Fixed-length integer keys -> Radix
- Uniformly distributed numeric data -> Bucket may be effective
- Parallel hardware -> sorting networks / parallel merge/radix variants
