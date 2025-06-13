"""
53:29.44
O(r*c * log(r*c)) worst case visit all cells, and heappush into a heap containing r*c cells
sO(r*c)
check solution after 5mins
the union find and binary search solutions are kinda crazy
man im bad with grafs
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        visited = [[False] * cols for _ in range(rows)]
        max_abs_diffs = [[math.inf] * cols for _ in range(rows)]

        # starting point
        max_abs_diffs[0][0] = 0
        to_visit = [(max_abs_diffs[0][0], 0, 0)]

        # iterate until is end is visited
        while to_visit and not visited[rows-1][cols-1]:

            # visit cell with minimum abs diff
            curr_max, curr_r, curr_c = heapq.heappop(to_visit)
            visited[curr_r][curr_c] = True

            # attempt to visit every direction
            for dr, dc in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
                new_r = curr_r + dr
                new_c = curr_c + dc
                # check if not IOOB and not visited
                if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c]:
                    new_max = abs(heights[new_r][new_c] - heights[curr_r][curr_c])
                    new_max = max(new_max, curr_max)
                    # check if new min found
                    if new_max < max_abs_diffs[new_r][new_c]:
                        max_abs_diffs[new_r][new_c] = new_max
                        heapq.heappush(to_visit, (new_max, new_r, new_c))

        return max_abs_diffs[rows-1][cols-1]
