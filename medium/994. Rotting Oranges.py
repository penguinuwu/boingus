"""
15:49.32
O(mn)
sO(mn)
remember to return=0 if all orangs are already rotten
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        good_orangs = 0
        future_rots = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good_orangs += 1
                elif grid[i][j] == 2:
                    future_rots.add((i, j))

        time = 0
        while future_rots and good_orangs > 0:
            time += 1
            curr_rots = future_rots
            future_rots = set()

            while curr_rots:
                curr_i, curr_j = curr_rots.pop()

                # affect other orangs
                for di, dj in ((0, -1), (-1, 0), (0, +1), (+1, 0)):
                    new_i = curr_i + di
                    new_j = curr_j + dj
                    if (
                        0 <= new_i < m
                        and 0 <= new_j < n
                        and grid[new_i][new_j] == 1
                    ):
                        grid[new_i][new_j] = 2
                        good_orangs -= 1
                        future_rots.add((new_i, new_j))

        if good_orangs > 0:
            return -1
        else:
            return time
