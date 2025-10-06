"""
6:47.97
O(n^2)
sO(n)
preread solution
the max is not always at the end
be careful of len(nums)=0 and len(nums)=1 case
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # store the longest sequence ending at each index
        dp = [1] * n
        answer = 1

        for curr in range(1, n):
            # find the longest sequence ending at curr
            for prev in range(curr):
                if nums[prev] < nums[curr]:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
            answer = max(answer, dp[curr])

        return answer
