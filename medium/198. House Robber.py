"""
32:00.47
O(n)
sO(1)
check solution after 14mins to optimize sO(n) -> sO(1)
dont need prev3 because prev1 has all (max(prev1+prev3, prev2))
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for n in nums:
            # rob 2 houses away with current house
            # or only rob previous house
            curr = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1


# [1,2,3,1]
#  1
#    2
#  1   3
#      4
#  1 2   1
#        3

# [2,7,9,3,1]
#  2
#    7
#  2   9
#     11
#  2 7   3
#       10
#    711   1
#         12
