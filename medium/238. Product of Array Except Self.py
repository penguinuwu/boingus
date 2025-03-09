class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview
        n = len(nums)
        results = [1] * n

        # carry over prefix
        curr = 1
        for i in range(n):
            results[i] *= curr
            curr *= nums[i]
        
        # carry over suffix
        curr = 1
        for i in range(n-1, -1, -1):
            results[i] *= curr
            curr *= nums[i]

        return results
