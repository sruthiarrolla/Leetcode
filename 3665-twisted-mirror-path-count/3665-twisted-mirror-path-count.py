from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(i, j, direction):
            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if direction == 0:  # Moving right
                    i += 1
                    direction = 1
                else:               # Moving down
                    j += 1
                    direction = 0

            if i >= m or j >= n:
                return None

            return i, j

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if i == m - 1 and j == n - 1:
                    continue

                ways = dp[i][j]

                # Try moving right
                pos = move(i, j + 1, 0)
                if pos is not None:
                    x, y = pos
                    dp[x][y] = (dp[x][y] + ways) % MOD

                # Try moving down
                pos = move(i + 1, j, 1)
                if pos is not None:
                    x, y = pos
                    dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]