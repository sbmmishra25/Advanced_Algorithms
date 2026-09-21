class SegmentTree:
    def __init__(self, values):
        n = 1
        while n < len(values):
            n *= 2
        self.n = n
        self.tree = [0] * (2 * n)
        self.tree[n:n + len(values)] = values
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, i, value):
        p = self.n + i
        self.tree[p] = value
        p //= 2
        while p:
            self.tree[p] = self.tree[2*p] + self.tree[2*p+1]
            p //= 2

    def query(self, left, right):
        left += self.n
        right += self.n + 1
        ans = 0
        while left < right:
            if left & 1:
                ans += self.tree[left]; left += 1
            if right & 1:
                right -= 1; ans += self.tree[right]
            left //= 2; right //= 2
        return ans