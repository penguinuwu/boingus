"""
13:57.30
O(n)
sO(n) technically i modify input array so that counts as extra space use
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_amount = 0

        for i in range(n):
            house3 = i - 3
            max_house3 = 0 if house3 < 0 else nums[house3]

            house2 = i - 2
            max_house2 = 0 if house2 < 0 else nums[house2]

            nums[i] += max(max_house2, max_house3)
            max_amount = max(max_amount, nums[i])

        return max_amount


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
