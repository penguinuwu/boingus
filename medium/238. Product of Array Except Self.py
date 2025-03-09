class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i, n in enumerate(nums):
            if i == 0:
                prefix.append(n)
            else:
                prefix.append(prefix[i-1] * n)

        suffix = []
        for i, n in enumerate(nums[::-1]):
            if i == 0:
                suffix.append(n)
            else:
                suffix.append(suffix[i-1] * n)

        results = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                results.append(suffix[n-2])
            elif i == n-1:
                results.append(prefix[n-2])
            else:
                results.append(prefix[i-1] * suffix[n-2-i])

        return results
