def count_inversions(a):
    def solve(arr):
        if len(arr) <= 1:
            return arr, 0
        m = len(arr) // 2
        left, x = solve(arr[:m])
        right, y = solve(arr[m:])
        merged, i, j, z = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                z += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, x + y + z
    return solve(list(a))[1]

print(count_inversions([2, 4, 1, 3, 5]))