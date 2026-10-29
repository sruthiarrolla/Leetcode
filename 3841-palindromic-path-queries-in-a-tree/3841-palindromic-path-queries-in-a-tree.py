from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str,
                       queries: List[str]) -> List[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        root_xor = [0] * n

        timer = 0
        stack = [(0, -1, 0, 0)]

        while stack:
            u, p, d, state = stack.pop()

            if state == 0:
                parent[u] = p
                depth[u] = d
                tin[u] = timer
                timer += 1

                root_xor[u] = (
                    (root_xor[p] if p != -1 else 0)
                    ^ (1 << (ord(s[u]) - ord('a')))
                )

                stack.append((u, p, d, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        stack.append((v, u, d + 1, 0))
            else:
                tout[u] = timer - 1

        LOG = n.bit_length()
        up = [[-1] * n for _ in range(LOG)]
        up[0] = parent[:]

        for k in range(1, LOG):
            for u in range(n):
                p = up[k - 1][u]
                if p != -1:
                    up[k][u] = up[k - 1][p]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree supporting subtree range-XOR updates
        # and point queries.
        class Fenwick:
            def __init__(self, size):
                self.size = size
                self.bit = [0] * (size + 2)

            def add(self, i, value):
                i += 1
                while i <= self.size + 1:
                    self.bit[i] ^= value
                    i += i & -i

            def range_update(self, left, right, value):
                self.add(left, value)
                if right + 1 < self.size:
                    self.add(right + 1, value)

            def point_query(self, i):
                i += 1
                result = 0
                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i
                return result

        bit = Fenwick(n)
        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                bit.range_update(tin[u], tout[u], delta)
                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                xor_u = root_xor[u] ^ bit.point_query(tin[u])
                xor_v = root_xor[v] ^ bit.point_query(tin[v])
                lca_mask = 1 << (ord(chars[w]) - ord('a'))

                mask = xor_u ^ xor_v ^ lca_mask

                # At most one character may have an odd frequency.
                answer.append((mask & (mask - 1)) == 0)

        return answer
        