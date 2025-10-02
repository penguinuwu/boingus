"""
3:54.59
O(n)
sO(n)
1 pass
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        missing_to_index = {}

        for i, v in enumerate(nums):
            if v in missing_to_index:
                return [missing_to_index[v], i]

            missing = target - v
            missing_to_index[missing] = i
