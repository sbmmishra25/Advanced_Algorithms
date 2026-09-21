class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        total = 0
        i += 1
        while i:
            total += self.bit[i]
            i -= i & -i
        return total

    def range_sum(self, left, right):
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left else 0)