"""
?
O(n*m)
sO(1)
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def area(start_row, start_col):
            area = 0
            frontier = {(start_row, start_col)}

            while frontier:
                row, col = frontier.pop()

                # non-land, skip
                if grid[row][col] != 1:
                    continue

                grid[row][col] = -1
                area += 1

                for drow, dcol in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
                    new_row = row + drow
                    new_col = col + dcol
                    if 0 <= new_row < m and 0 <= new_col < n:
                        if grid[new_row][new_col] == 1:
                            frontier.add((new_row, new_col))

            return area

        max_area = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    max_area = max(max_area, area(row, col))

        return max_area
