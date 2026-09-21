# String Algorithms — Complete Core

String algorithms range from exact pattern matching to multi-pattern search, text indexing, compression transforms, and string dynamic programming.

## Pattern matching
- Naive matching: O(nm) worst case.
- KMP: O(n+m), using a prefix/failure function.
- Z algorithm: O(n+m) for pattern/text constructions.
- Rabin-Karp: expected fast matching with rolling hashes; collisions require verification when exactness matters.
- Boyer-Moore family: skips characters using bad-character/good-suffix ideas.
- Aho-Corasick: trie plus failure links for multiple patterns.

## Indexing
- Trie: prefix queries.
- Suffix array + LCP: compact full-text index with many substring-query applications.
- Suffix tree: linear-size theoretical indexing under standard models.
- Suffix automaton: represents all substrings in a compact automaton.

## Other important algorithms
- Edit distance.
- Longest common subsequence.
- Longest common substring.
- Palindrome algorithms.
- Burrows-Wheeler transform.
- Manacher's algorithm for palindromic substrings.
- Rolling hash.
- Lexicographic ordering and suffix structures.

## Correctness and complexity
State the alphabet model, whether hashes are probabilistic, whether preprocessing is included, and whether the task asks for one match, all matches, or many patterns.
