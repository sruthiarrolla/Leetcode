class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        from collections import defaultdict

        logs.sort(key=lambda a: a[1])

        q = sorted([(t, i) for i, t in enumerate(queries)])

        count = defaultdict(int)
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0
        m = len(logs)

        for t, idx in q:
            start = t - x

            while right < m and logs[right][1] <= t:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans