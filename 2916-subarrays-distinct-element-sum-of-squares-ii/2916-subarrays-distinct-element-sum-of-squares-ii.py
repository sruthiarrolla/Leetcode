

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        sum1 = [0] * (2 * size)
        sum2 = [0] * (2 * size)
        lazy = [0] * (2 * size)

        def apply(node, l, r, val):
            length = r - l + 1
            sum2[node] = (
                sum2[node] + 2 * val * sum1[node]
                + val * val * length
            ) % MOD
            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            val = lazy[node]
            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            sum1[node] = (sum1[node * 2] + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2] + sum2[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, i, 1)
            last[x] = i
            ans = (ans + sum2[1]) % MOD

        return ans

        