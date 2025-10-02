"""
9:47.57
O(n)
sO(1)
forgot its 1passable
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # left-to-right (nums[0] * ... * nums[i-1])
        # skip first
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            result[i] *= left_product

        # right-to-left (nums[i+1] * ... * nums[-1])
        # skip last
        right_product = 1
        for i in range(n - 1 - 1, -1, -1):
            right_product *= nums[i + 1]
            result[i] *= right_product

        return result
