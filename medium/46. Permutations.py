"""
20:56.88
O(n * n!) because nPn = n!/(n-n)! = n! and copy of curr_list is O(n)
sO(n) slightly better because no set used but same order of magnitude
check solution after 2mins
swap solution but i prefer the previous simpler set solution
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def generate_permutes(start_idx):
            if start_idx == n:
                result.append(nums.copy())
                return

            for idx in range(start_idx, n):
                nums[start_idx], nums[idx] = nums[idx], nums[start_idx]
                # note: increase by start_idx and not just idx
                generate_permutes(start_idx + 1)
                nums[start_idx], nums[idx] = nums[idx], nums[start_idx]

        generate_permutes(0)
        return result
