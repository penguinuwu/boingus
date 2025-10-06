"""
20:08.40
O(n)
sO(1)
check solution after 4mins
beast solution
kandane algorithm but adding min tracking to account for negative products flipping signs
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1
        max_prod = 1
        max_total = -math.inf

        for n in nums:
            new_min_prod = min_prod * n
            new_max_prod = max_prod * n
            min_prod = min(n, new_min_prod, new_max_prod)
            max_prod = max(n, new_min_prod, new_max_prod)
            max_total = max(max_total, max_prod)

        return max_total
