"""
29:35.19
O(n)
sO(1)
check solution after 14mins to optimize sO(n) -> sO(1)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        max_house0 = nums[1] if 1 < n else 0
        max_house1 = nums[0]
        max_house2 = 0

        for i in range(2, n):
            curr_house = nums[i] + max(max_house1, max_house2)
            max_house2 = max_house1
            max_house1 = max_house0
            max_house0 = curr_house

        return max(max_house0, max_house1)


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
