"""
53:02.33
O(n^4) worst case but expected O(n^2 log n) due to sum of squares?!
sO(n^2)
math
"""

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # https://leetcode.com/problems/minimum-area-rectangle-ii/solutions/477751/clean-python-solution-with-explanation/
        # https://youtu.be/FcWK8CJReUo

        def get_distance(p1, p2) -> float:
            x1, y1 = p1
            x2, y2 = p2
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        def get_midpoint(p1, p2) -> Tuple[float]:
            x1, y1 = p1
            x2, y2 = p2
            return (x1 + x2) / 2, (y1 + y2) / 2

        # these diagonals can make a rectangle iff
        # 1. diagonals have same length
        # 2. diagonals have same midpoint
        buckets_of_diagonals = defaultdict(list)
        for i in range(len(points)):
            p1 = points[i]

            for j in range(i+1, len(points)):
                p3 = points[j]

                distance = get_distance(p1, p3)
                midpoint = get_midpoint(p1, p3)

                buckets_of_diagonals[(distance, midpoint)].append((p1, p3))

        min_area = math.inf
        for diagonals in buckets_of_diagonals.values():
            for i in range(len(diagonals)):
                p1, p3 = diagonals[i]

                for j in range(i+1, len(diagonals)):
                    p2, _ = diagonals[j]

                    area = get_distance(p1, p2) * get_distance(p2, p3)
                    min_area = min(min_area, area)

        return min_area if min_area != math.inf else 0
