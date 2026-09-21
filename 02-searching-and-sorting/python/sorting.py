def insertion_sort(a):
    a = list(a)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):
    if len(a) <= 1:
        return list(a)
    m = len(a) // 2
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]

def quick_sort(a):
    a = list(a)
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    return quick_sort([x for x in a if x < pivot]) + [x for x in a if x == pivot] + quick_sort([x for x in a if x > pivot])

if __name__ == "__main__":
    data = [7, 2, 9, 1, 5]
    print(insertion_sort(data))
    print(merge_sort(data))
    print(quick_sort(data))