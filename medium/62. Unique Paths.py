"""
9:58.45
O(m*n) without dp O(2^(m+n))
sO(m*n)
top-down dp
took 2mins to debug `i+1 >= m` -> `i+1 < m` grr
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # each cell represents number of unique paths from (i,j) to (m-1,n-1)
        cache = [[-1] * n for _ in range(m)]
        cache[m - 1][n - 1] = 1

        def dfs(i, j):
            if cache[i][j] != -1:
                return cache[i][j]

            # we can either go down or right
            total = 0

            # go down
            if i + 1 < m:
                total += dfs(i + 1, j)

            # go right
            if j + 1 < n:
                total += dfs(i, j + 1)

            cache[i][j] = total
            return total

        return dfs(0, 0)
