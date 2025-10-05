"""
11:16.05
O(n)
sO(1)
preread solution
missed the len(nums)==1 edge case be careful
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: rob all
        if len(nums) < 2:
            return sum(nums)

        def simulate_rob(start, end):
            prev1 = 0
            prev2 = 0

            for i in range(start, end):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr

            return prev1

        # since nums[0] and nums[n-1] are adjacent
        return max(
            # we either rob nums[0] .. n[n-2]
            simulate_rob(0, len(nums) - 1),
            # or rob nums[1] .. nums[n-1]
            simulate_rob(1, len(nums)),
        )
