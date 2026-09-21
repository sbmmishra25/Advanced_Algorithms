# Hashing — Complete Notes

## Core idea

A hash function maps a key to an index in a table. The objective is fast insertion, deletion and lookup under an appropriate load factor and collision strategy.

## Hash function families
- Division method
- Multiplication method
- Universal hashing
- Polynomial rolling hash
- Cryptographic hashes
- Perfect/minimal perfect hashing

## Collision resolution
### Separate chaining
Each table slot stores a bucket/list.

Expected lookup is O(1) under standard uniform hashing assumptions; worst case can be O(n).

### Open addressing
- Linear probing
- Quadratic probing
- Double hashing
- Robin Hood hashing
- Cuckoo hashing

## Advanced structures
- Bloom filter
- Counting Bloom filter
- Cuckoo filter
- Quotient filter
- Count-Min Sketch
- HyperLogLog

These structures trade exactness, memory, update cost or collision behavior for specialized workloads.

## Applications
- dictionaries/maps
- compiler symbol tables
- caches
- databases and indexes
- duplicate detection
- password storage with appropriate cryptographic password-hashing schemes
- web search and information retrieval
- distributed systems
- approximate membership and frequency estimation

## Important concepts
Load factor, collision probability, resizing, clustering, deletion markers, adversarial inputs and hash flooding.

## Practice
Implement chaining, linear probing, quadratic probing, double hashing, cuckoo hashing and a Bloom filter. Compare lookup behavior as load factor increases.
