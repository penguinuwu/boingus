"""
9:12.46
O(n)
sO(n)
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floors = len(cost)
        cost_from_step = {}

        def get_cost(step):
            if step >= floors:
                return 0

            step1 = step + 1
            if step1 not in cost_from_step:
                cost_from_step[step1] = get_cost(step1)

            step2 = step + 2
            if step2 not in cost_from_step:
                cost_from_step[step2] = get_cost(step2)

            return cost[step] + min(cost_from_step[step1], cost_from_step[step2])

        return min(get_cost(0), get_cost(1))
