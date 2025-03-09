class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview
        # https://leetcode.com/problems/product-of-array-except-self/solutions/65627/o-n-time-and-o-1-space-c-solution-with-explanation

        n = len(nums)
        prefix = 1
        suffix = 1
        results = [1] * n

        for i in range(n):
            results[i] *= prefix
            prefix *= nums[i]

            results[n-i-1] *= suffix
            suffix *= nums[n-i-1]

        return results
