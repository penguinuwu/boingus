"""
15:05.50
O(n)
sO(1)
1 pass beast
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # carry over from 677bc32
        # https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview
        # https://leetcode.com/problems/product-of-array-except-self/solutions/65627/o-n-time-and-o-1-space-c-solution-with-explanation

        n = len(nums)
        prefix = 1
        suffix = 1
        result = [1] * n

        for i in range(n):
            # left-to-right (nums[0] * ... * nums[i-1])
            result[i] *= prefix

            # right-to-left (nums[i+1] * ... * nums[-1])
            result[n - 1 - i] *= suffix

            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

        return result
