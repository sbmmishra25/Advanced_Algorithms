def linear_search(a, target):
    for i, x in enumerate(a):
        if x == target:
            return i
    return -1

def binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]
    print(linear_search(a, 7))
    print(binary_search(a, 7))