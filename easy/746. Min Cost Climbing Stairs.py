"""
10:16.47
O(n)
sO(n)
clean up using functool cache
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def get_cost(step):
            if step >= len(cost):
                return 0
            return cost[step] + min(get_cost(step + 1), get_cost(step + 2))

        return min(get_cost(0), get_cost(1))
