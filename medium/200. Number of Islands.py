class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0

        for i in range(m):
            for j in range(n):
                # skip water and visited
                if grid[i][j] == "0" or (i, j) in visited:
                    continue

                count += 1

                traverse = set()
                traverse.add((i, j))

                while traverse:
                    ii, jj = traverse.pop()
                    if grid[ii][jj] == "0" or (ii, jj) in visited:
                        continue

                    visited.add((ii, jj))

                    # visit 4 directions
                    for di, dj in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                        iii = ii + di
                        jjj = jj + dj
                        if 0 > iii or iii >= m or 0 > jjj or jjj >= n:
                            continue

                        # skip water and visited
                        if grid[iii][jjj] == "0" or (iii, jjj) in visited:
                            continue

                        traverse.add((ii + di, jj + dj))

        return count
