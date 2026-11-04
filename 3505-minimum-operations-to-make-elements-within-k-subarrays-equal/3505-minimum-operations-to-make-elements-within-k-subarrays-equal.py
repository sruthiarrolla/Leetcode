class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(tree, i, delta):
            while i <= m:
                tree[i] += delta
                i += i & -i

        def query(tree, i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & -i
            return res

        def kth(target):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and count[nxt] < target:
                    idx = nxt
                    target -= count[nxt]
                step >>= 1

            return idx + 1

        total = 0

        def add(v, delta):
            nonlocal total
            p = pos[v]
            update(count, p, delta)
            update(sums, p, v * delta)
            total += v * delta

        def get_cost():
            mid_idx = kth((x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = query(count, mid_idx)
            left_sum = query(sums, mid_idx)

            right_count = x - left_count
            right_sum = total - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        costs = []

        for i in range(n):
            add(nums[i], 1)

            if i >= x:
                add(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]
        