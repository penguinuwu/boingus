"""
21:56.33
O(n^2)
sO(n)
dont forget diagonals of rectangles
"""


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple, points))

        min_area = math.inf
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # skip all non-diagonals
                if x1 == x2 or y1 == y2:
                    continue

                # check if 2 more points exists to make diagonal->rectangle
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))

        return min_area if min_area != math.inf else 0
