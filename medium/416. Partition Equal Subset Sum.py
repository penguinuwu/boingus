"""
16:46.40
O(n*m) without dp O(2^n) where n=len(nums), m=sum(nums)/2
sO(n*m)
check solution after 3mins
didn't consider two equal subsets means each subset=total_sum/2 lmao
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        n = len(nums)
        cache = {}

        def dfs(start_idx, target_sum):
            if (start_idx, target_sum) in cache:
                return cache[(start_idx, target_sum)]
            if target_sum == 0:
                cache[(start_idx, target_sum)] = True
                return True
            if start_idx == n:
                cache[(start_idx, target_sum)] = False
                return False

            result = dfs(start_idx + 1, target_sum) or dfs(
                start_idx + 1, target_sum - nums[start_idx]
            )
            cache[(start_idx, target_sum)] = result
            return result

        return dfs(0, total_sum // 2)
