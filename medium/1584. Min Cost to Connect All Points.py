"""
?
O(n^2)
sO(n)
preread solution
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        n_connected = 0
        connected = [False] * n
        min_costs = [math.inf] * n
        min_cost = 0

        curr_point = 0
        min_costs[0] = 0

        while n > n_connected and curr_point != -1:
            n_connected += 1
            min_cost += min_costs[curr_point]
            connected[curr_point] = True

            min_dist_point = math.inf, -1
            for i, (skip, point) in enumerate(zip(connected, points)):
                if not skip:
                    next_dist = dist(*points[curr_point], *point)
                    min_costs[i] = min(min_costs[i], next_dist)

                    if min_dist_point[0] > min_costs[i]:
                        min_dist_point = min_costs[i], i
            curr_point = min_dist_point[1]

        return min_cost
