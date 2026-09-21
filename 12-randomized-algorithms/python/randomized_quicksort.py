import random

def randomized_quicksort(a, seed=42):
    rng = random.Random(seed)
    a = list(a)

    def sort(lo, hi):
        if lo >= hi:
            return
        p = rng.randint(lo, hi)
        a[p], a[hi] = a[hi], a[p]
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        sort(lo, i - 1)
        sort(i + 1, hi)

    sort(0, len(a) - 1)
    return a

if __name__ == "__main__":
    print(randomized_quicksort([5,2,9,1,7]))